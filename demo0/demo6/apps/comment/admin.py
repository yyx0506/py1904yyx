from django.contrib import admin
import xadmin
from .models import *
# Register your models here.
xadmin.site.register(Comment)
# xadmin.site.register(HeroInfo,HeroInfoAdmin)
