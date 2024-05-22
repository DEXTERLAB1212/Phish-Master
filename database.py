import os
import getpass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from utils.color import color
from utils.banner import banner
from utils.dots import dots
# Import the models
from models.users.user import User
from models.info.info import Info
from models.media.media import Media
from models.creds.creds import Creds


# Get the current working directory
cwd = os.getcwd()

# Initialize the Flask app with the database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(cwd, 'PhishMaster.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

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

# Create the Info table if it doesn't exist
try:
    with app.app_context():
        inspector = inspect(db.engine)
        if 'info' not in inspector.get_table_names():
            # Explicitly create the Info table
            Info.__table__.create(db.engine)
            print()
            print(color.ColorPrinter.magenta("Creating Info Table"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("Info Table Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("Info Table already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating Info table: {e}"))
    
# Create the Media table if it doesn't exist
try:
    with app.app_context():
        inspector = inspect(db.engine)
        if 'media' not in inspector.get_table_names():
            # Explicitly create the Media table
            Media.__table__.create(db.engine)
            print()
            print(color.ColorPrinter.magenta("Creating Media Table"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("Media Table Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("Media Table already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating Media table: {e}"))

# Create the Creds table if it doesn't exist
try:
    with app.app_context():
        inspector = inspect(db.engine)
        if 'creds' not in inspector.get_table_names():
            # Explicitly create the Creds table
            Creds.__table__.create(db.engine)
            print()
            print(color.ColorPrinter.magenta("Creating Creds Table"), end=" ")
            dots.print_dots(10)
            print()
            print(color.ColorPrinter.green("Creds Table Created Successfully"))
        else:
            print()
            print(color.ColorPrinter.yellow("Creds Table already exists"))
except Exception as e:
    print(color.ColorPrinter.red(f"Error creating Creds table: {e}"))