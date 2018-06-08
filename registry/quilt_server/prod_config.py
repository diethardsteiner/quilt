# Copyright (c) 2017 Quilt Data, Inc. All rights reserved.

"""
Config file for prod/stage. Overrides values in config.py.
"""
import os

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

REGISTRY_HOST = os.environ['REGISTRY_HOST']
CATALOG_HOST = os.environ['CATALOG_HOST']

CATALOG_URL = 'https://%s' % CATALOG_HOST

PACKAGE_BUCKET_NAME = os.environ['PACKAGE_BUCKET_NAME']

# Optional
MIXPANEL_PROJECT_TOKEN = os.getenv('MIXPANEL_PROJECT_TOKEN')
DEPLOYMENT_ID = os.getenv('DEPLOYMENT_ID')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
ENABLE_USER_ENDPOINTS = bool(os.getenv('ENABLE_USER_ENDPOINTS', ''))
