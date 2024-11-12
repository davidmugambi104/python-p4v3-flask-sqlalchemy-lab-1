from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Create a MetaData instance for managing table definitions
metadata = MetaData()

# Initialize Flask-SQLAlchemy with the metadata
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    # SerializerMixin gives us a way to easily serialize objects to dicts
    # Add custom __repr__ method for string representation
    def __repr__(self):
        return f"Earthquake(id={self.id}, magnitude={self.magnitude}, location='{self.location}', year={self.year})"
