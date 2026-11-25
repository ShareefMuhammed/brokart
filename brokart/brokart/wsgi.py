"""
WSGI config for brokart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brokart.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brokart.settings")
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82

application = get_wsgi_application()
