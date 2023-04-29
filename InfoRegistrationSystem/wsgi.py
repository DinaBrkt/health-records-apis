"""
WSGI config for InfoRegistrationSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys

sys.path.append('C:\\Users\\Dina Ibrahim\\PycharmProjects\\InfoRegistrationSystem\\InfoRegistrationSystem')
sys.path.append('C:\\Users\\Dina Ibrahim\\PycharmProjects\\InfoRegistrationSystem\\registerApp')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InfoRegistrationSystem.settings')

application = get_wsgi_application()
