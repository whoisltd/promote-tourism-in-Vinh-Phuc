from app import db
from datetime import datetime
from geoalchemy2 import Geometry
# from app import login
from werkzeug.security import generate_password_hash, check_password_hash

class tourist_area(db.Model):
    __tablename__ = 'tourist_area'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    geom = db.Column(Geometry('POLYGON', srid=4326))
    # One to many
    place = db.relationship('place', backref='tourist_area', lazy='True')
class place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=False)
    geom = db.Column(Geometry('POLYGON', srid=4326))
    # One to Many
    service = db.relationship('services', backref='place', lazy=True)
    # Many to Many
    # place = db.relationship('Place', backref='users', lazy=True)

class posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=False)
    id_place = db.Column(db.Integer, db.ForeignKey('places.id'))
    id_review = db.Column(db.Integer, db.ForeignKey('reviews.id'))

class reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    review = db.Column(db.Text, nullable=False)
    id_place = db.Column(db.Integer, db.ForeignKey('places.id'))
    id_service = db.Column(db.Integer, db.ForeignKey('services.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

class services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    id_place = db.Column(db.Integer, db.ForeignKey('places.id'))
    type = db.Column(db.String, nullable=False)
    # Many to Many
    # place = db.relationship('places', backref='services', lazy=True)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    role = db.Column(db.String(20))
    __mapper_args__ = {
        'polymorphic_on': role
    }
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)

class user(users):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

class admin(users):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

# @login.user_loader
# def load_user(id):
#     return users.query.get(int(id))


    # One to Many
    # user = db.relationship('User', backref='posts', lazy=True)
    # Many to Many
    # place = db.relationship('Place', backref='users', lazy=True)
    