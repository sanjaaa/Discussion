from django.contrib import admin
#from .models import user_account
from .models import discussion
from .models import comment
# Register your models here.
#admin.site.register(user_account)
admin.site.register(discussion)
admin.site.register(comment)