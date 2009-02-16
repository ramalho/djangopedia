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

from inspect import getmembers, isclass, getclasstree, getargspec

field_types = [c for n,c in getmembers(models.fields, isclass) if issubclass(c,Field)]

def show_all_classes():

    for name, klass in getmembers(models.fields, isclass):
        isField = issubclass(klass, models.fields.Field)
        print ' +'[isField], name
        
def show_tree():
    tree = getclasstree(field_types)
    for item in tree:
        print item
    
def export_field_args():
    args, varargs, varkw, defaults = getargspec(Field.__init__)
    def_args = args[-len(defaults):]
    print '\t'+'\t'.join(def_args)
    print 'Field\t'+'\t'.join([repr(v) for v in defaults])

def show_field_args():
    args, varargs, varkw, defaults = getargspec(Field.__init__)
    args, def_args = args[:-len(defaults)], args[-len(defaults):]
    if args:
        print '-'*40, 'ARGS WITHOUT DEFAULTS'
        for arg in args: 
            print arg,
        print
    if def_args:
        print '-'*40, 'ARGS WITH DEFAULTS'
        for arg, default in zip(def_args, defaults):
            print '%s = %r' % (arg, default)

ARG_SEQ = getargspec(Field.__init__)            

def export_field_args(klass):
    args, varargs, varkw, defaults = getargspec(klass.__init__)
    if len(args) > len(defaults):
        defaults = list(defaults)
        while len(args) > len(defaults):
            defaults.insert(0, '!')
    print '\t'+'\t'.join(args)
    print klass.__name__+'\t'+'\t'.join([repr(v) for v in defaults])

            
            
export_field_args(Field)
export_field_args(models.CharField)


        