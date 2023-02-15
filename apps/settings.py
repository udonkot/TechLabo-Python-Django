import imp


import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'project_static')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    [
        os.path.join(BASE_DIR, "static"),
    ]
)
