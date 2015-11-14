#Records all buy sell transactions for each user
import evelink
import sys
import select
import tty
import termios
import time
import datetime
import MySQLdb
import string

#connects to master to get user accounts
dbOver=MySQLdb.connect(host="localhost", user="root", passwd="password", db="EveCalcMaster")
cursOver=dbOver.cursor()

#inserts a transaction into the appropriate table (buy or sell)
def insertInto(table, entry, curs, db):
    transID=str(entry['id'])
    itemID=str(entry['type']['id'])
    time=entry['timestamp']
    timestamp=datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    itemName=entry['type']['name']
    price=str(entry['price'])
    quantity=str(entry['quantity'])
    stationID=str(entry['station']['id'])
    stationName=entry['station']['name']
    char=entry['char']['name']
    clientUnmoded=entry['client']['name']
    client=clientUnmoded.translate(string.maketrans("",""), string.punctuation)
    query="INSERT INTO "+table+" (`transactionID`, `timestamp`, `itemID`, `itemName`, `price`, `quantity`, `stationID`, `char`, `client`, `stationName`) VALUES ('"+transID+"', '"+timestamp + "','"+itemID + "','"+itemName + "','"+price + "','"+quantity + "','"+stationID + "','"+char + "','"+client + "','"+stationName + "')"
    #print query
    curs.execute(query)
    historyQuery="INSERT INTO "+table+"History (`transactionID`, `timestamp`, `itemID`, `itemName`, `price`, `quantity`, `stationID`, `char`, `client`, `stationName`) VALUES ('"+transID+"', '"+timestamp + "','"+itemID + "','"+itemName + "','"+price + "','"+quantity + "','"+stationID + "','"+char + "','"+client + "','"+stationName + "')"
    curs.execute(historyQuery)
    db.commit()
    


#Gets each users api and loads all new transactions into the appropriate table using insertInto
def loader(apiKey, vCode, user, wallet):
    db=MySQLdb.connect(host="localhost", user="root", passwd="password", db=str(user)+"EveCalc")
    curs=db.cursor()
    api=evelink.api.API(api_key=(str(apiKey), vCode))
    corp=evelink.corp.Corp(api=api)
    transactionPull=corp.wallet_transactions(account=wallet, limit="2560")
    transDic=transactionPull.result
    #print transDic
    #insertInto('Sell', transDic[0])
    for trans in transDic:
        if trans['action']=='sell':
            checkHistQuery="SELECT transactionID FROM SellHistory WHERE transactionID="+str(trans['id'])
            curs.execute(checkHistQuery)
            histArr=curs.fetchone()
            if not histArr:
                insertInto('Sell', trans, curs, db)
        if trans['action']=='buy':
            checkHistQuery="SELECT transactionID FROM BuyHistory WHERE transactionID="+str(trans['id'])
            curs.execute(checkHistQuery)
            histArr=curs.fetchone()
            if not histArr:
                insertInto('Buy', trans, curs, db)

#Iterates through all users
generalQuery="SELECT * FROM `Users` WHERE 1"
cursOver.execute(generalQuery)
userArr=cursOver.fetchall()
for row in userArr:
    api=row[0]
    print api
    vCode=row[1]
    print vCode
    user=row[2]
    wallet=row[5]
    loader(api, vCode, user, wallet)
