#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response

app = Flask( __name__ )

@app.route( '/' )
def index() :
    return 'Replika - Accueil'


if __name__ == '__main__' :
    app.run( debug = True )