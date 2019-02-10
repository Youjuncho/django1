from .views import *
from django.urls import path


app_name = 'blog'

urlpatterns = [
    # 뷰클래스 등록시 뷰클래스.as_view()로 등록
    path('', Index.as_view(), name = 'index'),
    # DetailView 클래스는 객체를 추출하기 위해 'pk' 매개변수를 사용함. (원래는 int:id~ 이런식으로 사용했던 것처럼, 뷰함수에서는 pk를 사용한다고 생각하면 된다.)
    # 127.0.0.1:8000/blog/글번호/
    path('<int:pk>/', Detail.as_view(), name = 'detail'), # detail뷰 함수 사용하겠다.
    # 127.0.0.1:8000/blog/posting/
    path('posting/', Posting.as_view(), name = 'posting')
    ]