# -*- coding: utf-8 -*-
"""The main config file for Superset

All configuration in this file can be overridden by providing a superset_config
in your PYTHONPATH as there is a ``from superset_config import *``
at the end of this file.
"""

from flask_appbuilder.security.manager import AUTH_DB, AUTH_REMOTE_USER


# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
ROW_LIMIT = 50000
VIZ_ROW_LIMIT = 10000
# max rows retrieved by filter select auto complete
FILTER_SELECT_ROW_LIMIT = 10000
SUPERSET_WORKERS = 2  # deprecated
SUPERSET_CELERY_WORKERS = 32  # deprecated

SUPERSET_WEBSERVER_ADDRESS = '0.0.0.0'
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT = 60  # deprecated
EMAIL_NOTIFICATIONS = False
CUSTOM_SECURITY_MANAGER = None
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ---------------------------------------------------------

# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'  # noqa

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'

# The limit of queries fetched for query search
QUERY_SEARCH_LIMIT = 1000

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []

# Whether to run the web server in debug mode or not
DEBUG = False
FLASK_USE_RELOAD = True

# Whether to show the stacktrace on 500 error
SHOW_STACKTRACE = True

# Extract and use X-Forwarded-For/X-Forwarded-Proto headers?
ENABLE_PROXY_FIX = False

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_REMOTE_USER

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# When using REMOTE_USER Auth, setup the cas server
CAS_SERVER = 'https://sso.xx.com'
CAS_LOGIN_ROUTE = '/cas/login'
CAS_AFTER_LOGIN = 'index'

# ---------------------------------------------------
# Roles config
# ---------------------------------------------------
# Grant public role the same set of permissions as for the GAMMA role.
# This is useful if one wants to enable anonymous users to view
# dashboards. Explicit grant on specific datasets is still required.
PUBLIC_ROLE_LIKE_GAMMA = False

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'superset/translations'
# The allowed translation for you app
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    'it': {'flag': 'it', 'name': 'Italian'},
    'fr': {'flag': 'fr', 'name': 'French'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'ja': {'flag': 'jp', 'name': 'Japanese'},
    'de': {'flag': 'de', 'name': 'German'},
    'pt_BR': {'flag': 'br', 'name': 'Brazilian Portuguese'},
    'ru': {'flag': 'ru', 'name': 'Russian'},
}

# An instantiated derivative of werkzeug.contrib.cache.BaseCache
# if enabled, it can be used to store the results of long-running queries
# in SQL Lab by using the "Run Async" button/feature
RESULTS_BACKEND = None

# Roles that are controlled by the API / Superset and should not be changes
# by humans.
ROBOT_PERMISSION_ROLES = ['Public', 'Gamma', 'Alpha', 'Admin', 'sql_lab']

CONFIG_PATH_ENV_VAR = 'SUPERSET_CONFIG_PATH'

# When not using gunicorn, (nginx for instance), you may want to disable
# using flask-compress
ENABLE_FLASK_COMPRESS = True