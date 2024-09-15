"""Connect to Postgres Database"""
import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# import environment variables from .env
load_dotenv()

# create the flask application with the same name as the file
app = Flask(__name__)

# tell flask which database you want to connect to. pulls values from .env
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('db_owner')}:{os.getenv('db_pass')}@localhost/{os.getenv('db_name')}"

# flask-sqlalchemy instance; used for all database interactions
db = SQLAlchemy(app)

# verify the db connection is successful
with app.app_context():
    # attempt to connect to db, print msgs if successful
    try:
        # run SQL query to verify connection (see how we use the db instance?)
        db.session.execute(text("SELECT 1"))
        print(f"\n\n----------- Connection successful!")
        print(f" * {os.getenv('name')} successfully connected to database: {os.getenv('db_name')}!")
    # failed to connect to db, provide msgs & error
    except Exception as error:
        print(f"\n\n----------- Connection failed!")
        print(f" * Unable to connect to database: {os.getenv('db_name')}.")
        print(f" * ERROR: {error}")
