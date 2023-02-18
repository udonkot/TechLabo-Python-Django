import imp


import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    [
        os.path.join(BASE_DIR, "staticfiles"),
    ]
)
