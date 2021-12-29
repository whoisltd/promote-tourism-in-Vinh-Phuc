from flask_admin.contrib.sqla.view import ModelView
from sqlalchemy.orm import backref
import wtforms
from app import db
from datetime import datetime
from geoalchemy2.types import Geometry
from wtforms.validators import ValidationError
from flask_admin.form.upload import FileUploadField
import imghdr

# from app import login
from werkzeug.security import generate_password_hash, check_password_hash

class Tourist_area(db.Model):
    __tablename__ = 'tourist_area'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    geom = db.Column(Geometry('POINT', srid=4326))
    posts = db.relationship('Posts', backref='tourist_area', lazy='dynamic')
    services = db.relationship('Services', backref= 'tourist_area', lazy= 'dynamic')
    place = db.relationship('Place', backref = 'tourist_area', lazy= 'dynamic')

    # def __repr__(self):
    #     return (self.name)
    def __str__(self):
        return self.name or ''

    
class Place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=True)
    geom = db.Column(Geometry('POINT', srid=4326))
    id_tourist_area = db.Column(db.Integer, db.ForeignKey('tourist_area.id'))
    id_post = db.Column(db.Integer, db.ForeignKey('posts.id'))

    # def __repr__(self):
    #     return '<Place %r>' % (self.title)
    def __str__(self):
        return self.title or ''

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=True)
    content = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=True)
    id_tourist_area = db.Column(db.Integer, db.ForeignKey('tourist_area.id'))
    id_place = db.Column(db.Integer, db.ForeignKey('place.id'))

    # def __repr__(self):
    #     return '<Posts %r>' % (self.title)
    def __str__(self):
        return self.title or ''
        

class PostsView(ModelView):
    form__columns = [ 'id', 'title', 'content', 'image', 'area' ]



class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    rating = db.Column(db.Integer)
    review = db.Column(db.Text, nullable=True)
    id_tourist_area = db.Column(db.Integer, db.ForeignKey('tourist_area.id'))
    id_place = db.Column(db.Integer, db.ForeignKey('place.id'))
    id_service = db.Column(db.Integer, db.ForeignKey('services.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

class Services(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    geom = db.Column(Geometry('POINT', srid=4326))
    id_tourist_area = db.Column(db.Integer, db.ForeignKey('tourist_area.id'))
    type = db.Column(db.String, nullable=True)
    # Many to Many
    # place = db.relationship('places', backref='services', lazy=True)

    # def __repr__(self):
    #     return '<Services %r>' % (self.name)
    def __str__(self):
        return self.name or ''

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=True)
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

class User(Users):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

class Admin(Users):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))

# @login.user_loader
# def load_user(id):
#     return users.query.get(int(id))


    # One to Many
    # user = db.relationship('User', backref='posts', lazy=True)
    # Many to Many
    # place = db.relationship('Place', backref='users', lazy=True)
    