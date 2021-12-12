from flask import render_template
from flask import Flask
from app import app
from app.models import *
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

class MyView(BaseView):
    @expose('/admin/home')
    def index(self):
        return self.render('layout.html')

admin = Admin(app=app, name= "VPhuc Travel", template_mode="bootstrap3")
admin.add_view(PostsView(Posts, db.session))
admin.add_view(ModelView(Services, db.session))
admin.add_view(ModelView(Place, db.session))   

