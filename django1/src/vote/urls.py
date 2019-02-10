
from django.urls import path
# from .views import index, detail, result, vote, qregister, qupdate, qdelete 이제 너무 많아서 *로 바꿔주겠다.
from .views import *

# 하위 URL Conf.
# app_name : 하위 URLConf 파일에 등록된 URL들의 그룹명 (따라서 상위 URLConf와 같은 파일 이름이어도, 얘는 하위 URLConf 파일에 등록된 누구이다!라고 이해할수 있음)
# urlpatterns : URL과 뷰함수를 리스트형태로 등록하는 변수
app_name = 'vote'
# 기본주소 : 127.0.0.1:8000/vote/
urlpatterns = [
    # django1의 urls.py에 처음 추가한 path('vote/', include('vote.urls')) : 'vote/'를 앞에 해놨기 때문에  기본적으로
    # 기본주소 : 127.0.0.1:8000/vote/으로 작동된다. 따라서 path('')으로 해도 djanog1의 페이지와 겹치지 않는다. 
    # 웹 클라이언트가 127.0.0.1:8000/vote. 요청시 index 뷰함수 호출
    path('', index, name = 'index'),
    # 127.0.0.1:8000/vote/숫자/
    # <:> --> 왼쪽 = 데이터타입 / 오른쪽 = 어디다가 넣을건지
    path('<int:q_id>/', detail, name = 'detail'),
    path('vote/', vote, name = 'vote'), # 앞에는 vote/ 내 마음대로 넣어준것
    path('result/<int:q_id>/', result, name = 'result'), # 위에 이미 int:q_id가 있기 떄문에, 위에서 순서대로 작업하기 때문에 겹치면 작동이 안된다. 따라서 앞에 result를 작성. 
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # 127.0.0.1:8000/vote/qr까지 작성해 주어야 나온다.
    path('qr/', qregister, name = "qr"), # qr/주소로 들어오면 qregister 뷰함수를 호출하게 된다. qr이라고 별칭을 넣어주자.
    # 127.0.0.1:8000/vote/qu/Question객체의 id값
    path('qu/<int:q_id>/', qupdate, name = "qu"),
    # 127.0.0.1:8000/vote/qd/Question객체의 id값
    path('qd/<int:q_id>/', qdelete, name = 'qd'),
    # 127.0.0.1:8000/vote/cr/
    path('cr/', cregister, name = 'cr'),
    # 127.0.0.1:8000/vote/cu/Choice객체id값
    path('cu/<int:c_id>/', cupdate, name = 'cu'),
    path('cd/<int:c_id>/', cdelete, name = 'cd'),
    ] 