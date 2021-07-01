#!/usr/bin/env python
"""
An extremely simple app to demo how to deploy to kubernetes
"""

import os
import logging
import sys
from flask import Flask
import json_logging
from .api import views
import yaml
from .extensions import db
import psycopg2

# Disable startup banner
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None



def setup_logging(APP_NAME, app):
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))


class Config(object):
    """Maps environment variables and other runtime configurations into code"""
    APP_NAME = 'sample-kube-app' # TODO this should be the project name, likely the same as the repo it's in
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    ENV = os.environ.get('ENVIRONMENT_NAME', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy complains that turning this on adds significant overhead.
                                           # Probably not useful unless you use the orm portion anyway.


def create_app(config_object=Config):
    """
    An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """

    app = Flask(config_object.APP_NAME)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    setup_logging(app.config['APP_NAME'], app)
    # verify db is up
    try:
        conn = psycopg2.connect(dsn=app.config['SQLALCHEMY_DATABASE_URI'])
    except psycopg2.OperationalError as e:
        # bail if it isn't
        print(e)
        sys.exit(-1)
    conn.close()
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.main_blueprint)
    # other blueprints could be added here, but there should be only one per µservice unless you have a good reason
    return None
