from django.contrib import admin
# 우리가 만든 vote 데이터베이스에 접근할 수 있도록 허용하기 위해 admin.py에 들어와서 작업
from .models import *

admin.site.register(Choice)
admin.site.register(Question)
