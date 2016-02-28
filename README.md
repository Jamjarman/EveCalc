# EveCalc
A simple webapp with python backend to calculate profit from industrial manufacturing in EveOnline

The purpose of this calculator is to calculate overall profit made from industry, including actual material buy price, and final sell price.

#Set Up
To use this calculator 3 things must be done. First the host computer must be set up to use a mysql database, this computer will host a db for the master table of users, as well as each users personal database.

These databases should be copied from the included files in the db directory. 

The files in the html directory should be used to host a web front end. This front end will allow users to be added given an api key (their database must be set up manually) and then for that user to log in and view their information.

Finally the python files which update and control the databases must be updated. On a linux machine this can be done by adding update.sh as a deamon. This will update all api keys and calculate the database. It is recommended that this be done no more than every half hour.

#Known issues

Sales tax is currently not included, industry job costs however are.
Long term industrialists will have issues due to the length of the buy/sell api vs the industry job api. The system backdates by finding average 30 day price from CREST in instances where a material which is bought or sold cannot be found in the users inventory.

