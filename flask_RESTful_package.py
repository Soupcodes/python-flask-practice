from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Homepage(Resource):
    def get(self):
        return {'msg': 'Welcome to Chill #96'}

    def post(self):
        some_json = request.get_json()
        return {'you_sent':some_json}, 201

class Multi(Resource):
    def get(self, num):
        return {'result': num*10}, 201


api.add_resource(Homepage, '/')
api.add_resource(Multi, '/multiply/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)