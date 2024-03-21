#from https://www.youtube.com/watch?v=PXo3AAquPy0 - not done obv
from flask import flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class sendMessage(Resource):
    def get(self):
        return {"message": "message from container 1"}
    
    api.add_resource(sendMessage, '/')

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)