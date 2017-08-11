import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SECRET_KEY = 'flask is fun !'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgis:postgis@localhost:5432/TestGIS2'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    