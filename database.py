from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from utils.color import color
from utils.banner import banner
from utils.dots import dots

# Get the current working directory
cwd = os.getcwd()

# Initialize the Flask app with the database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(cwd, 'PhishMaster.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Print banner
banner.print_banner()

# Check if the database file exists, create if not
db_path = os.path.join(cwd, 'PhishMaster.sqlite3')
try:
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print()
            print(color.ColorPrinter.magenta("Creating Database"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("Database Created Successfully.."))
    else:
        print()
        print(color.ColorPrinter.yellow("Database already exists."))
except Exception as e:
    print(color.ColorPrinter.red(f"Error: {e}"))