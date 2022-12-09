# db_host_key = "db_host"
# db_user_key = "db_user_key"
# db_passwd_key = "db_passwd"
# db_database_key = "db_database"

# auth = os.getenv(auth_key, default=None)


# db_host = os.getenv(db_host_key, default=None)
# db_user = os.getenv(db_user_key, default=None)
# db_pwd = os.getenv(db_passwd_key, default=None)
# db_database = os.getenv(db_database_key, default=None)
import mysql.connector


auth = "OTAzNzAzODA2NDE4NzU5NzEw.GzoEty.RpPoVSutPs7Qd8mCaiK3Usa_aJYuqMSurQvGH8"



db_host="remotemysql.com"
db_user="ojo1RYm6Dz"
db_pwd="KjtXXab7Is"
db_database="ojo1RYm6Dz"

prefix = "cul "
host = "http://localhost:5000/"

# conn = mysql.connector.connect(
#         host=config.db_host,
#         user=config.db_user,
#         passwd=config.db_pwd,
#         database=config.db_database)
# cur = conn.cursor()