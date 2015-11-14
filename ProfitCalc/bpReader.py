#Updates personal bp collection of user to include ME and TE
import evelink
import select
import sys
import time
import datetime
import string
import MySQLdb

#Connect to database master to get user information
dbOver=MySQLdb.connect(host="localhost", user="root", passwd="password", db="EveCalcMaster")
cursOver=dbOver.cursor()


#GEts ME and TE and inserts into users table
def insertInto(entry, curs, db):
    print entry
    bpID=entry['type_id']
    bpName=entry['type_name']
    ME=entry['material_efficiency']
    TE=entry['time_efficiency']
    checkQuery="SELECT * FROM `BPStats` WHERE bpID="+str(bpID)
    curs.execute(checkQuery)
    row=curs.fetchone()
    print row
    entryQuery=""
    if row:
        print "duplicate exists"
        if row[2]>ME:
            ME=row[2]
        if row[3]>TE:
            TE=row[3]
        removeQuery="DELETE FROM `BPStats` WHERE bpID="+str(bpID)
        curs.execute(removeQuery)
    entryQuery=entryQuery+"INSERT INTO BPStats (`bpID`, `bpName`, `ME`, `TE`) VALUES ('"+str(bpID)+"', '"+bpName+"', '"+str(ME)+"', '"+str(TE)+"')"
    curs.execute(entryQuery)
    db.commit()

#Loads each users information, connecting to their database and then loading all blueprints into their table
def loader(keyID, vCode, user):
    db=MySQLdb.connect(host="localhost", user="root", passwd="password", db=user+"EveCalc")
    curs=db.cursor()
    api=evelink.api.API(api_key=(keyID, vCode))
    corp=evelink.corp.Corp(api=api)
    bprints=corp.blueprints()
    keyset=bprints.result.keys()
    for i in keyset:
        insertInto(bprints.result[i], curs, db)

#iterates through all users in the master table
generalQuery="SELECT * FROM `Users` WHERE 1"
cursOver.execute(generalQuery)
userArr=cursOver.fetchall()
for row in userArr:
    api=row[0]
    vCode=row[1]
    user=row[2]
    wallet=row[5]
    loader(api, vCode, user)
