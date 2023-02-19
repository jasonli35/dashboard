# Add the necessary imports
import mysql.connector as mysql
import os
import mysql.connector as mysql
from dotenv import load_dotenv

''' Environment Variables '''
load_dotenv('credentials.env')

# Read Database connection variables
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']


# Connect to the db and create a cursor object
db =mysql.connect(user=db_user, password=db_pass, host=db_host)
cursor = db.cursor()
cursor.execute("CREATE DATABASE if not exists TechAssignment5;")
cursor.execute("USE TechAssignment5;")

cursor.execute("drop table if exists Ideas;")
try:
   cursor.execute("""
   CREATE TABLE Ideas (
       id          integer  AUTO_INCREMENT PRIMARY KEY,
       title        VARCHAR(100) NOT NULL,
       competitors VARCHAR(100) NOT NULL,    
       price       VARCHAR(100) NOT NULL,
       cost        VARCHAR(100) NOT NULL,
       market_size  VARCHAR(100)
   );
 """)
except RuntimeError as err:
   print("runtime error: {0}".format(err))

query = "INSERT into Ideas (title, competitors, price, cost, market_size) values (%s, %s, %s, %s,%s)"
values = [
  ('mapSocial', ' social media sites', '0.0' ,'0.0', '10000000'),
  ('window', 'Companies making smart furniture system', '500.00', '200.00', '5000000'),
  ('plug', 'Switch bot', '120.00', '40.00', '1000000000'),
  ('decentralized_version_of_uber', ' Uber, Lyft, Postmates and Grubhub', '0.00', '0.00', '0'),
  ('Purifier', ' Dyson, Xiaomi, or Coway', '300', '100', '80'),
]
cursor.executemany(query, values)
db.commit()
