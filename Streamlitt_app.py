import pymysql

# Database connection details 
db_host = p274783438042-nq2c2m@gcp-sa-cloud-sql.iam.gserviceaccount.com
db_user = mysql-csgroupproject8-4
db_password = +/iHlkkQ=YxD#Ip7
db_name = cs-group-project-8-4:europe-west6:mysql-csgroupproject8-4

# Connect to the cloud database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = connection.cursor()