#!/usr/bin/env python

### boilerplate to run scripts from a Django project sub-directory
import sys, os
here = os.path.abspath(os.path.split(__file__)[0])
above = os.path.split(here)[0]
sys.path.append(above)

from django.core.management import setup_environ
import settings
setup_environ(settings)
#### /boilerplate

from lab.app1.models import EmptyModel

print dir(EmptyModel)
