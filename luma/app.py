# coding=utf-8
"""Author: Michal Wrona
Copyright (C) 2016 ACK CYFRONET AGH
This software is released under the MIT license cited in 'LICENSE.txt'

Contains flask application definition.
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(
        os.path.join(os.path.dirname(config), app.config['DATABASE']))
    db.init_app(app)

    return app
