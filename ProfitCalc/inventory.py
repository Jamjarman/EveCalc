import evelink
import sys
import select
import time
import datetime
import string
import MySQLdb
import json
import math
import urllib2
#Connects to master to get users
dbOver=MySQLdb.connect(host="localhost", user="root", passwd="password", db="EveCalcMaster")
cursOver=dbOver.cursor()

#Removes used/sold materials from inventory and returns total cost of materials used
def materialsInInventory(itemID, quan, curs, db):
    query="SELECT * FROM Inventory WHERE itemID="+str(itemID)
    curs.execute(query)
    itemArr=curs.fetchall()
    priceTotal=0
    for item in itemArr:
        price=item[4]
        quantity=item[5]
        ID=item[0]
        if quan>0:
            if quan<quantity:
                updatedQuantity=quantity-quan
                priceTotal+=quan*price
                removeQuery="UPDATE `Inventory` SET `quantity`="+str(updatedQuantity)+" WHERE `ID`="+str(ID)
                curs.execute(removeQuery)
                db.commit()
                quan=0
            elif quan>=quantity:
                priceTotal+=quantity*price
                quan-=quantity
                removeQuery="DELETE FROM Inventory WHERE `ID`="+str(ID)
                curs.execute(removeQuery)
                db.commit()
    if quan>0:
        getPastQuery="SELECT price FROM BuyHistory WHERE itemID="+str(itemID)
        curs.execute(getPastQuery)
        pastPrices=curs.fetchall()
        total=0.0
        counter=0
        for pricePoint in pastPrices:
            total+=pricePoint[0]
            counter+=1
        if total*counter>0:
            avgPrice=total/counter
            priceTotal+=avgPrice*quan
        else:
            itemHistData=urllib2.urlopen("https://public-crest.eveonline.com/market/10000002/types/"+str(itemID)+"/history/").read()
            itemHistDictTotal=json.loads(itemHistData)
            #print itemHistDictTotal.keys()
            itemHistDict=itemHistDictTotal['items']
            counter=0
            total=0.0
            for i in range(0,30):
                counter+=1
                total+=itemHistDict[i]['avgPrice']
            avgPrice=total/counter
            priceTotal+=avgPrice*quan
    return priceTotal
#Catalogues production, getting jobs, removing mats from inventory, and adding products to inventory
def catalogueProduction(curs, db):
    pullQuery="SELECT * FROM Industry WHERE 1"
    curs.execute(pullQuery)
    indyData=curs.fetchall()
    for row in indyData:
        jobID=row[0]
        #print "Job ID: "+str(jobID)
        acquired=row[2]
        bpID=row[3]
        itemID=row[5]
        itemName=row[6]
        #print "Item: "+str(itemName)
        runs=row[7]
        #print "Runs: "+str(runs)
        price=row[8]
        #print "Cost: "+str(price)
        bpQuery="SELECT * FROM BPSDE WHERE bpID="+str(bpID)
        curs.execute(bpQuery)
        bpSDE=curs.fetchone()
        matArr=json.loads(bpSDE[1])
        buildQuant=bpSDE[3]
        #print "Build Quantity: "+str(buildQuant)
        quantity=runs*buildQuant
        #print "Production Quantity: "+str(quantity)
        matBuildPrice=0
        bpStatQuery="SELECT `ME` FROM `BPStats` WHERE bpID="+str(bpID)
        ME=0.0
        try:
            curs.execute(bpStatQuery)
            ME=float(curs.fetchone()[0])/100.0
        except:
            ME=.02
        #print "ME: "+str(ME)
        facilityStatQuery="SELECT `MEBonus` FROM `ManCost` WHERE 1"
        curs.execute(facilityStatQuery)
        MEFacility=curs.fetchone()[0]/100
        for mat in matArr:
            matID=mat['typeID']
            #print "Material ID: "+str(matID)
            matQuant=mat['quantity']
            #print "Single Run Mats: "+str(matQuant)
            matQuant=max(math.ceil((matQuant*runs)*(1-ME-MEFacility)), runs)
            #print "Actual Mats: "+str(matQuant)
            matPriceTotal=materialsInInventory(matID, matQuant, curs, db)
            #print "Total Mat Price: "+str(matPriceTotal)
            matBuildPrice+=matPriceTotal
        #print "Material Build Cost: "+str(matBuildPrice)
        price+=matBuildPrice
        #print "Total Price: "+str(price)
        price=price/quantity
        #print "Price Per Item: "+str(price)
        insertQuery="INSERT INTO Inventory (`ID`, `itemID`, `itemName`, `source`, `price`, `quantity`, `acquired`) VALUES ('"+str(jobID)+"', '"+str(itemID)+"', '"+itemName+"', 'Industry', '"+str(price)+"', '"+str(quantity)+"', '"+str(acquired)+"')"
        curs.execute(insertQuery)
        removeQuery="DELETE FROM Industry WHERE jobID="+str(jobID)
        curs.execute(removeQuery)
        db.commit()
        #print "---------------------------------------------------------------------"
        #print
            
#Adds purchases to inventory
def cataloguePurchase(curs, db):
    pullQuery="SELECT * FROM Buy WHERE 1"
    curs.execute(pullQuery)
    buyData=curs.fetchall()
    for row in buyData:
        ID=row[0]
        itemID=row[2]
        itemName=row[3]
        source="Buy Order "+row[9]
        price=row[4]
        quantity=row[5]
        time=row[1]
        insertQuery="INSERT INTO Inventory (`ID`, `itemID`, `itemName`, `source`, `price`, `quantity`, `acquired`) VALUES ('"+str(ID)+"','"+str(itemID)+"','"+itemName+"','"+source+"','"+str(price)+"','"+str(quantity)+"', '"+str(time)+"')"
        deleteQuery="DELETE FROM Buy WHERE transactionID="+str(ID)
        curs.execute(deleteQuery)
        curs.execute(insertQuery)
        db.commit()

#Removes sales from inventory and adds to profits
def catalogueSales(curs, db):
    pullQuery="SELECT * FROM Sell WHERE 1"
    curs.execute(pullQuery)
    salesArr=curs.fetchall()
    for sale in salesArr:
        transID=sale[0]
        timestamp=sale[1]
        itemID=sale[2]
        itemName=sale[3]
        priceSold=sale[4]
        quantitySold=sale[5]
        location=sale[9]
        buyPrice=materialsInInventory(itemID, quantitySold, curs, db)
        indBuyPrice=buyPrice/quantitySold
        profit=priceSold*quantitySold-buyPrice
        insertQuery="INSERT INTO Profit (`ID`, `timestamp`, `itemID`, `itemName`, `buyPrice`, `sellPrice`, `quantity`, `profit`, `source`, `saleLocation`) VALUES ('"+str(transID)+"', '"+str(timestamp)+"', '"+str(itemID)+"', '"+itemName+"', '"+str(indBuyPrice)+"', '"+str(priceSold)+"','"+str(quantitySold)+"','"+str(profit)+"','Industry','"+location+"')"
        curs.execute(insertQuery)
        removeQuery="DELETE FROM Sell Where transactionID="+str(transID)
        curs.execute(removeQuery)
        db.commit()

#Calls all functions for each user
def inventoryAccount(user):
    db=MySQLdb.connect(host="localhost", user="root", passwd="password", db=user+"EveCalc")
    curs=db.cursor()
    cataloguePurchase(curs, db)
    catalogueProduction(curs, db)
    catalogueSales(curs, db)

#Iterates through users and call inventoryAccount
generalQuery="SELECT * FROM `Users` WHERE 1"
cursOver.execute(generalQuery)
userArr=cursOver.fetchall()
for row in userArr:
    api=row[0]
    vCode=row[1]
    user=row[2]
    wallet=row[5]
    inventoryAccount(user)
