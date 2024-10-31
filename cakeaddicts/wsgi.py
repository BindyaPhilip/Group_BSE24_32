"""
WSGI config for cakeaddicts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# settings_module = (
#     "cakeaddicts.deployment"
#     if "WEBSITE_HOSTNAME" in os.environ
#     else "cakeaddicts.settings"
# )

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application

# Determine which settings file to use based on DJANGO_ENV
settings_module = (
    "cakeaddicts.deployment"  # Production settings
    if os.environ.get("DJANGO_ENV") == "production"
    else "cakeaddicts.production"  # Staging settings
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
