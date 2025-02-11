from .base import *

DEBUG = True

ALLOWED_ORIGINS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
  "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}