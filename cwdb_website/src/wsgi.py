"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

from dj_static import Cling,MediaCling


application = get_wsgi_application()
<<<<<<< HEAD
application =  Cling(MediaCling(application))
=======
>>>>>>> 1d7d3d2cc3a457e2febeeb2064e7dc67c0e24e2f

