"""django1 URL Configuration <!--url설정하는 곳이다.-->

"""
from django.contrib import admin
from django.urls import path, include
# from bookmark.views import * : 해당 파일에 들어있는 모든 변수, 함수, 클래스 임포트 -->일일히 추가하면서 작성하기 귀찮으면 사용.대신 단점이 있음
# bookmark/views.py의 index, booklist, getbook함수 임포트
from bookmark.views import index, booklist, getbook

# url.py : 웹 클라이언트의 요청을 분석해 특정한 뷰를 호출하는 파일
# urlpatterns : URL과 뷰함수를 등록 및 관리하는 변수
# 리스트 형태로 저장, URL 등록 시 path함수를 통해 urlpatterns의 요소로 추가
# path(URL주소(문자열), 호출할 뷰함수/클래스 이름)

# 기본주소 : 127.0.0.1:8000
urlpatterns = [
    # 웹 클라이언트가 127.0.0.1:8000/admin으로 요청한 경우
    # 관리자 사이트 뷰가 실행되도록 등록
    path('admin/', admin.site.urls),
    # 사용자가 접근할 수 있도록 url에다가 index를 등록한 것.
    # 웹 클라이언트가 127.0.0.1:8000/ 으로 요청한 경우 index 뷰함수 호출
    # ''으로 하면 기본 주소가 들어감.
    path('', index), # 1
    path('booklist/', booklist), # 2
    # 127.0.0.1:8000/숫자값/ 으로 요청한 경우
    # getbook 뷰함수 호출. bookid 매개변수에 숫자값을 대입
    # URL에서 매개변수로 사용할 값을 분리하는 방법 : <값의 타입:매개변수이름> --> 아까 두번째는 필요없는데, 넣어주었기 때문에 url에서 매개변수를 사용하기 위해 <> 이렇게 사용
    path('<int:bookid>/', getbook), # 3
    # 투표어플리케이션 사용할 하위 URLConf 등록
    # 웹 클라이언트가 127.0.0.1:8000/vote/로 시작하는 모든 요청을 vote폴더에 있는 urls.py에 등록된 urlpatterns로 처리하도록 등록
    path('vote/', include('vote.urls')),
    # 127.0.0.1:8000/cl/로 시작하는 모든 요청을 customlogin/urls.py에 넘겨줌
    path('cl/', include('customlogin.urls')),
    # 127.0.0.1:8000/blog로 시작하는 모든 요청을 blog/urls.py로 처리
    path('blog/', include('blog.urls')),
    # social_django 어플리케이션의 하위 URL Conf 등록
    path('auth/', include('social_django.urls', namespace = 'social')) # 우리가 처리할게 아니라, social_django.urls에서 처리를 할것이다.라고 작성
]
# 미디어파일을 저장 및 요청처리 하기 위한 설정

# settings.py에 설정된 변수를 가져오기 위해 임포트
from django.conf import settings
# MEDIA_URL과 MEDIA_ROOT를 연결하기 위한 함수
from django.conf.urls.static import static
# 파일 요청 URL과 실제 저장된 파일 경로를 매칭
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
