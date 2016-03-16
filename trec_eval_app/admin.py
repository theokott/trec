from django.contrib import admin
from trec_eval_app.models import *

# Register your models here.

admin.site.register(Run)
admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(Track)