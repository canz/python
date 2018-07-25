import random
import yaml
import pymysql


for i in range(5):
    print(random.random())

with open("C:\\Users\\steph\\github\\python\\settings.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)

# Connect
db = pymysql.connect(host="192.168.10.240",
                     user="testuser",
                     passwd="demopass",
                     db="pythontest")
cursor = db.cursor()

# Execute SQL select statement
cursor.execute("SELECT * FROM user_details")

# Commit your changes if writing
# In this case, we are only reading data
# db.commit()

# Get the number of rows in the resultset
numrows = cursor.rowcount

# Get and display one row at a time
for x in range(0, numrows):
    row = cursor.fetchone()
    print (row[0], "-->", row[1])

# Close the connection
db.close()
