#Imports blue print information from .yaml file for later access to materials etc.
import yaml
import MySQLdb
import string
import json

#Connect to database adn create cursor
db=MySQLdb.connect("localhost", "root", "password", "EveCalc")
curs=db.cursor()

#Attempts to load information about each blueprint
def loadBP(bp):
    try:
        bpID=bp['blueprintTypeID']
        mats=bp['activities']['manufacturing']['materials']
        matsEnc=json.dumps(mats)
        production=bp['activities']['manufacturing']['products'][0]
        itemID=production['typeID']
        quantity=production['quantity']#Insert into blueprint table
        query="INSERT INTO BPSDE (`bpID`, `materials`, `itemID`, `quantity`) VALUES ('"+str(bpID)+"','"+matsEnc+"','"+str(itemID)+"','"+str(quantity)+"')"
        curs.execute(query)
        db.commit()
    except:#Executes if blueprint is missing certain quantities (occurs with some T2 Blueprints
        print "Error occured on:"
        print bp
    
#Get yaml file of blueprints and prepare to load data
export=open('blueprints.yaml')
datamap=yaml.safe_load(export)
export.close()
keyList=datamap.keys()
for key in keyList:#iterate through contents of yaml and load blueprints
    loadBP(datamap[key])
