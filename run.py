import json

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/lottery"
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'{self.username}-{self.user_id}-{self.password}-{self.email}-{self.firstname}-{self.lastname}'


# db.create_all()
# user1=User(username='ganesh11',password='kafle42',email='ganesh@gmail.com',firstname='ganesh',lastname='kafle')
# db.session.add(user1)
# db.session.commit()

class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    email = fields.Email()
    firstname = fields.Str()
    lastname = fields.Str()


class UserInfo(Resource):

    def get(self):
        users = User.query.all()
        schema = UserSchema(many=True)
        output = schema.dump(users)
        return jsonify(output)

    def post(self):
        first_name = request.json['Firstname']
        last_name = request.json['Lastname']
        email = request.json['Email']
        user_name = request.json['Username']
        password = request.json['Password']
        user = User(username=user_name,password=password,email=email,firstname=first_name,lastname=last_name)
        db.session.add(user)
        db.session.commit()
        return 'Successfully inserted'

class UserOperation(Resource):

    def get(self, id):
        user = User.query.get(id)
        schema = UserSchema()
        output = schema.dump(user)
        return jsonify(output)

    # def put(self, id):
    #     user = User.query.get(id)
    #     if user.firstname != request.json['Firstname']:
    #         schema = UserSchema(only='firstname')
    #         store = schema.load(user)
    #         db.session.add(store)
    #         db.session.commit()
    #         return 'Successfully updated'
    #     else:
    #         return 'Firstname already exist'
    #     #
        # if user.lastname != request.json['Lastname']:
        #     schema = UserSchema(only='lastname')
        #     store = schema.load(user)
        #     db.session.add(store)
        #     db.session.commit()
        #     return 'Successfully updated'
        # else:
        #     return 'Lastname already exist'
        #
        # if user.email == request.json['Email']:
        #     db.session.add(user.email)
        #     db.session.commit()
        #     return user.email
        # if user.username == request.json['Username']:
        #     db.session.add(user.username)
        #     db.session.commit()
        #     return user.username

    def delete(self, id):
        user = UserInfo.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return ('Successfully deleted')





api.add_resource(UserInfo, '/user')
api.add_resource(UserOperation,'/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
