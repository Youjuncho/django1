# admin.py : 해당 어플리케이션에 정의된 모델클래스를 관리자사이트에서
# 데이터를 추가/수정/삭제를 할 수 있도록 설정하는 파일
from django.contrib import admin

# 현재폴더(.)에 models.py 안의 Bookmark 모델클래스를 임포트
# 현재 bookmark라는 폴더에 admin.py와 models.py가 같이 있기 때문에 현재폴더를 의미하는 .을 이용 
from .models import Bookmark

# admin.site.register(모델클래스명)
admin.site.register(Bookmark)
