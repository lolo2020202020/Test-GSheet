import pymysql

# Database connection details 
db_host = "34.65.8.211"
db_user = "mysql-csgroupproject8-4"
db_password = "+/iHlkkQ=YxD#Ip7"
db_name = "products-"

# Connect to the cloud database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = connection.cursor()

# Performs SQL operations here


# Close the connection
connection.close()