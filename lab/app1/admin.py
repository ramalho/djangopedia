from django.contrib import admin, databrowse, auth
from lab import app1

admin.site.register(app1.models.EmptyModel)
admin.site.register(app1.models.OneFieldModel)

databrowse.site.register(app1.models.EmptyModel)
databrowse.site.register(app1.models.OneFieldModel)

databrowse.site.register(auth.models.User)
databrowse.site.register(auth.models.Group)
databrowse.site.register(auth.models.Permission)

