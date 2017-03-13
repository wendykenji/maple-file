#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-12 20:16:21 (CST)
# Last Update:星期一 2017-3-13 16:56:18 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Flask, send_from_directory, current_app
from .admin import admin
import os


def create_app(config):
    app = Flask(__name__)
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Flask(__name__, template_folder=templates, static_folder=static)
    app.config.from_object(config)
    register(app)
    return app


def register(app):
    from .server.urls import site
    app.register_blueprint(site, url_prefix='/api')
    register_extensions(app)

    @app.route('/images/<path:name>')
    def photo(name):
        config = current_app.config
        return send_from_directory(config['UPLOAD_FOLDER'], name)


def register_extensions(app):
    from .extension import db, login, middleware
    db.init_app(app)
    login.init_app(app)
    middleware.init_app(app)
    admin.init_app(app)
