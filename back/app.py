#-*- coding:utf-8 -*-

from flask import g
from threading import Thread
from flask import Flask
from flask_cors import CORS
from flask_restplus import reqparse, abort, Api, Resource
import db_init
import predict


app = Flask(__name__)
CORS(app)
api = Api(app)

name_space = api.namespace('api', description='Main APIs')

api.app.config['RESTPLUS_JSON'] = {
    'ensure_ascii': False
}

@name_space.route("/reports")
class Reports(Resource):
    def get(self):
        return db_init.get_reports()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        parser.add_argument('answer', type=str, required=True)
        parser.add_argument('change_answer', type=str, required=True)
        args = parser.parse_args()
        db_init.post_report(args)
        return args

@name_space.route("/report/<int:id>")
class Report(Resource):
    def get(self, id):
        try:
            data = db_init.get_report(id)
        except TypeError:
            data = abort(400)
        return data

    def delete(self, id):
        try:
            db_init.get_report(id)
            db_init.delete_report(id)
            data = {'message': '삭제 완료'}
        except TypeError:
            data = abort(400, message='데이터가 존재하지 않습니다')
        return data

@name_space.route("/getMessage")
class Predict(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userMsg')
        args = parser.parse_args()
        data = predict.input_data(['Docker', args['userMsg']])
        return {"answer": data}

db_init.create_table()
db_init.data_in()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
