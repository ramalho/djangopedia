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

from django.db import models
from django.db.models.fields import Field

from inspect import getmembers, isclass, getclasstree

for name, klass in getmembers(models.fields, isclass):
    isField = issubclass(klass, models.fields.Field)
    print ' +'[isField], name
        
field_types = [c for n,c in getmembers(models.fields, isclass) if issubclass(c,Field)]
tree = getclasstree(field_types)
for item in tree:
    print item
    
