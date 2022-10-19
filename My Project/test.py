from flask import Flask, render_template
from config import host, user, password, database
import psycopg2, requests

app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template('index.html')

if __name__ == ('__main__'):
   app.run (debug=True)



url = "https://solana-gateway.moralis.io/nft/mainnet/2camF6sXuq4eQ2h2815xiA2r3BvoYNQbFztbLNymiwsq/metadata"
headers = {

    "accept": "application/json",
    "X-API-Key": "Pd4PYmtSlrXbWeFRBCvaqCAWCuwHzfvwyx3AOZH9EAc3xVGBwmwJXd9wEZFWApgV"

}

response = requests.get(url, headers=headers)

print(response.text)



connection = psycopg2.connect(database=database, user=user, password=password, host=host)

cursor = connection.cursor()

cursor.execute("""SELECT * from metaplex""")

# Fetch all rows from database

record = cursor.fetchall()

print("Data from Database:- ", record)