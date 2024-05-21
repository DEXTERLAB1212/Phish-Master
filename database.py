import os
import getpass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from utils.color import color
from utils.banner import banner
from utils.dots import dots

# Get the current working directory
cwd = os.getcwd()

# Initialize the Flask app with the database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(cwd, 'PhishMaster.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Import the User model from the correct location
from models.users.user import User

# Print banner
banner.print_banner()

# Check if the database file exists, create if not
db_path = os.path.join(cwd, 'PhishMaster.sqlite3')
try:
    with app.app_context():
        if not os.path.exists(db_path):
            db.create_all()
            print()
            print(color.ColorPrinter.magenta("Creating Database"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("Database Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("Database already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating database: {e}"))

# Create the User table if it doesn't exist
try:
    with app.app_context():
        inspector = inspect(db.engine)
        if 'user' not in inspector.get_table_names():
            # Explicitly create the User table
            User.__table__.create(db.engine)
            print()
            print(color.ColorPrinter.magenta("Creating User Table"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("User Table Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("User Table already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating User table: {e}"))

# Check if the User table has any entries
def user_table_has_entry():
    return db.session.query(User.id).first() is not None
  
# Create new User 
def create_user():
  # Get user input for username and password
  print()
  username = input(color.ColorPrinter.cyan("Enter Username: "))
  print()
  password = getpass.getpass(color.ColorPrinter.cyan("Enter Password: "))
  # Create a User instance and add it to the database
  user = User(username=username, password=password)
  db.session.add(user)
  db.session.commit()
  print()
  print(color.ColorPrinter.green("New User Created Successfully"))

with app.app_context():
    if user_table_has_entry():
        print()
        print(color.ColorPrinter.yellow("User already exists"))
        print()
        create_new_user = input(color.ColorPrinter.cyan("User table is not empty. Do you want to create a new user? (y/n): "))
        if create_new_user.lower() == 'y':
            create_user()
        else:
            print()
            print(color.ColorPrinter.yellow("No new user created."))
    else:
        create_user()