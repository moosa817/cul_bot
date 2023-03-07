import os


auth = "" #discord bot auth token
db_host = "" #mysql databasehost
db_database = "" #mysql database db
db_pwd = "" #mysql db pwd
db_user = "" #mysql db user
rapid_api_key = "" #rapid api key 

auth = os.getenv("auth",default=auth)
db_host = os.getenv("db_host",default=auth)
db_database = os.getenv("db_database",default=auth)
db_user = os.getenv("db_user",default=auth)
db_pwd = os.getenv("db_pwd",default=db_pwd)
rapid_api_key = os.getenv("rapid_api_key",default=rapid_api_key)





prefix = "cul "
host = "https://cul-bot.moosa817.repl.co/"