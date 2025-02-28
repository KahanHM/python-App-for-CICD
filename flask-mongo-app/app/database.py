from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = "mongodb://mongo:27017/userdb"
    mongo.init_app(app)
