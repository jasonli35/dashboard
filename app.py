from fastapi import FastAPI, Request, Form
from fastapi.responses import Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn
from fastapi.responses import RedirectResponse
from urllib.request import urlopen
from urllib.request import urlopen

import mysql.connector as mysql
import os
import mysql.connector as mysql
from dotenv import load_dotenv



app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

#route for main page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
   with open("index.html") as html:
       return HTMLResponse(content=html.read())

#route for dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
   with open("dashboard.html") as html:
       return HTMLResponse(content=html.read())


load_dotenv('credentials.env')

# Read Database connection variables
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


add_one_idea_query = "INSERT into Ideas (title, competitors, price, cost, market_size) values (%s, %s, %s, %s,%s)"
#Need to add /addidea, /deleteidea
#post route for add idea
@app.post("/addidea/{title}/{competitors}/{price}/{cost}/{market_size}")
def add_ideas(title:str, competitors:str, price:str,cost:str,market_size:str):
    # Connect to the db and create a cursor object
    db =mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = db.cursor()
    # cursor.execute("USE TechAssignment5;")
    value = (title,competitors,price,cost,market_size)
    cursor.execute(add_one_idea_query,value)
    db.commit()
    db.close()
     


#delete idea by idea
@app.delete("/deleteidea/{title}")
def delete_idea(title:str):
    # Connect to the db and create a cursor object
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5;")
    query = "DELETE FROM Ideas WHERE title=%s;"
    value = [(title)]
    cursor.execute(query, value)
    db.commit()
    db.close()
    return title

#modify market size by title
@app.put("/modify/{title}/{size}")
def modify_idea(title:str, size:str):
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5;")
    query = "UPDATE Ideas SET market_size=%s WHERE title=%s;"
    value = (size,title)
    cursor.execute(query, value)
    db.commit()
    db.close()

#modify market cost by title
@app.put("/modify/cost/{title}/{cost}")
def modify_idea(title:str, cost:str):
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5;")
    query = "UPDATE Ideas SET cost=%s WHERE title=%s;"
    value = (cost,title)
    cursor.execute(query, value)
    db.commit()
    db.close()

#modify market price by title
@app.put("/modify/cost/{title}/{price}")
def modify_idea(title:str, price:str):
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5;")
    query = "UPDATE Ideas SET price=%s WHERE title=%s;"
    value = (price,title)
    cursor.execute(query, value)
    db.commit()
    db.close()

#modify market competitor by title
@app.put("/modify/cost/{title}/{competitor}")
def modify_idea(title:str, competitor:str):
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5;")
    query = "UPDATE Ideas SET competitor=%s WHERE title=%s;"
    value = (competitor,title)
    cursor.execute(query, value)
    db.commit()
    db.close()
   

#return all idea from db
@app.get("/allIdeas")
def get_all_idea():
    db =mysql.connect(user=db_user, password=db_pass, host=db_host)
    cursor = db.cursor()
    cursor.execute("USE TechAssignment5")
    cursor.execute("select * from Ideas;")
    # fetch the remaining rows
    records = cursor.fetchall()
     # disconnecting from server
    db.close()
    response = {}
    for index, row in enumerate(records):
       response[index] = {
           "id": row[0],
           "title": row[1],
           "competitors": row[2],
           "price": row[3],
           "cost": row[4],
           "market_size": row[5]
       }
    return JSONResponse(response)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=6543, reload=True)



