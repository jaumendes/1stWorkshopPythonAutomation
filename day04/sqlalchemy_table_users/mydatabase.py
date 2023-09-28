# jaumendes
# https://medium.com/@sandyjtech/creating-a-database-using-python-and-sqlalchemy-422b7ba39d7e

# Step 1: Import the necessary modules

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


# Step 2: Establish a database connection

database_url = 'sqlite:///your_database_names.db'

# Create an engine to connect to a SQLite database
engine = create_engine(database_url)

#will return engine instance
Base = declarative_base()

# Step 3: Define your data model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Step 4: Create the database tables
Base.metadata.create_all(engine)

# Step 5: Insert data into the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Inserting a new user into the database
new_user = User(username='Ssaadndy', email='saanddys@gmail.com', password='codoaol-password')
session.add(new_user)
session.commit()

# Step 6: Query data from the database
# Example: Querying all users from the database
all_users = session.query(User).all()
for i in all_users:
    print(i)

# Example: Querying a specific user by their username
user = session.query(User).filter_by(username='Sandy').first()

for u in session.query(User).all():
    print (u.__dict__)
    
# Step 7: Close the session
session.close()
