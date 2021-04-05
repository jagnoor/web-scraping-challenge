from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_NASA_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_NASA=mars_NASA_data)


@app.route("/scrape")
def scrape():
    # Running the Scrape Function
    mars_data = scrape_mars.scrape_info()

    # Updating the Mongo Database
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Going Back to Homepage
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

