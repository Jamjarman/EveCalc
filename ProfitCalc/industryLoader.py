#Imports industry jobs of all users in the master database
import evelink
import sys
import select
import time
import datetime
import MySQLdb
import string

#Connects to master to get user information
dbOver=MySQLdb.connect(host="localhost", user="root", passwd="password", db="EveCalcMaster")
cursOver=dbOver.cursor()

counter=0
newLastQuery=0

#Inserts industry job into table for user
def insertInto(entry, key, curs, db):
    installer=entry['installer']['name']
    time=entry['begin_ts']
    timestamp=datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    jobID=str(counter)
    bpID=str(entry['blueprint']['type']['id'])
    bpName=entry['blueprint']['type']['name']
    itemID=str(entry['product']['type_id'])
    itemName=entry['product']['name']
    cost=str(entry['cost'])
    activity=str(entry['activity_id'])
    runs=str(entry['runs'])
    query="INSERT INTO Industry (`jobID`, `installer`, `timestamp`, `bpID`, `bpName`, `itemID`, `itemName`, `runs`, `cost`, `activity`) VALUES ('"+str(key) +"','"+installer +"','"+timestamp +"','"+bpID +"','"+bpName +"','"+itemID+"','"+itemName+"','"+runs +"','"+cost +"','"+activity +"')"
    curs.execute(query)
    historyQuery="INSERT INTO IndustryHistory (`jobID`, `installer`, `timestamp`, `bpID`, `bpName`, `itemID`, `itemName`, `runs`, `cost`, `activity`) VALUES ('"+str(key) +"','"+installer +"','"+timestamp +"','"+bpID +"','"+bpName +"','"+itemID+"','"+itemName+"','"+runs +"','"+cost +"','"+activity +"')"
    curs.execute(historyQuery)
    db.commit()

#Gets api of user and calls insert into
def loader(apiKey, vCode, user):
    db=MySQLdb.connect(host="localhost", user="root", passwd="password", db=user+"EveCalc")
    curs=db.cursor()
    api=evelink.api.API(api_key=(apiKey, vCode))
    corp=evelink.corp.Corp(api=api)
    indyHist=corp.industry_jobs_history()
    jobList=indyHist.result
    IndyJobKeyArr=jobList.keys()
    for key in IndyJobKeyArr:
        if jobList[key]['activity_id']==1:
            checkHistQuery="SELECT jobID FROM IndustryHistory WHERE jobID="+str(key)
            curs.execute(checkHistQuery)
            histArr=curs.fetchone()
            if not histArr:
                insertInto(jobList[key], key, curs, db)

#Iterates through all users in master
generalQuery="SELECT * FROM `Users` WHERE 1"
cursOver.execute(generalQuery)
userArr=cursOver.fetchall()
for row in userArr:
    api=row[0]
    vCode=row[1]
    user=row[2]
    wallet=row[5]
    loader(api, vCode, user)

