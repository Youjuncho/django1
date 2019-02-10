# views.py : View의 기능을 하는 클래스/함수를 정의하는 파일
# render (함수) : 웹 클라이언트에게 HTML파일을 넘겨줄때 사용하는 함수
from django.shortcuts import render

# 뷰 함수 정의 시 첫 번째 매개변수를 반드시 request로 설정해야 함.
# request : 사용자의 요청 정보, <form>으로 넘겨준 데이터, 로그인정보, 세션정보, 요청방식(GET, POST) 등이 저장됨.

# 총 세가지의 작업을 할 것이다.
# 1) HTML 파일을 전송하는 메인페이지
def index(request): # index 뷰를 요청하는 함수를 만들어 준것.(index란 이름은 내가 정해준 것.)
    # render(request(매개변수), 클라이언트에게 줄 HTML 파일경로, HTML에 전달할 값)
    # 1.네이버같이 많은 클라이언트가 한번에 들어올 수 있기 때문에, 처음에 request로 해줘서 하나의 클라이언트에 줄 것을 의미
    # 2.클라이언트한테 어떤 HTML파일을 넘겨줄 것이냐 -->지금 만들어 놓지 않은 index.html 을 쓴다고 했으니, 직접 만들어준다.(t-b-index.html)
    # 3.HTML에 전달할 값을 사전형으로 전달해준다. (사전형 = {})
    return render(request, 'bookmark/index.html', {'a' : 'hello', 'b' : [1,2,3,4,'django']})
    
# 여기까지가 1) 해당

# Bookmark 모델클래스 임포트
# from bookmark.models import Bookmark 도 같은 것. 대신 이건 현재 위치에서 가져오는 것이 아니라, 직접 가져오는것(?)
from .models import Bookmark # 현재 위치에서 bookmark.models를 가져온것

# 2) Bookmark 모델 클래스에 저장된 모든 객체를 HTML에 추가하는 페이지
def booklist(request):
    # 모델 클래스.objects.get() : 데이터베이스에 해당 모델클래스로 저장된 객체 중 특정조건을 만족하는 객체 한개를 추출하는 함수
    # 모델 클래스.objects.all() : 데이터베이스에 해당 모델클래스로 저장된 모든 객체를 추출
    # 모델 클래스.objects.filter() : 데이터베이스에 특정조건을 만족하는 모든 객체를 리스트형태로 추출
    # 모델 클래스.objects.exclude() : 데이터베이스에 특정조건을 만족하지 않는 모든객체를 리스트형태로 추출
    
    # Bookmark 모델 클래스의 모든 객체를 리스트형태로 list변수에 저장
    # 즉, 데이터베이스에 지금 (네이버,구글,다음) 세 개가 저장되어 있기 때문에 list변수에는 세 개가 있다.
    list = Bookmark.objects.all() 
    return render(request, 'bookmark/booklist.html', {'objs' : list})
    # 역시나 bookmark/booklist.html을 만들어준다.
    # objs는 새로만든 booklist.html 파일에서 사용할 수 있는 변수 이름이다. 여기서 작성한 list의 변수값으로 만들어줬기 때문이다.
    
# 여기까지가 2) 해당

# 3) Bookmark 모델 클래스의 개체 중 한 개를 HTML에 추가하는 페이지
# 뷰함수에 매개변수 추가 시, URLConf에서 추가 설정을 해야됨
def getbook(request, bookid): # request는 무조건 써야하고, 두번째부터는 내가 쓰고 싶으면 쓰고 안쓰고 싶으면 안써도됨.
    # 객체 한개를 추출할 때, 객체별로 저장된 고유한 id값을 이용해 추출함 (네이버=1,다음=2...이랬던거)
    # 어떤 id값을 가진 객체를 요청했는지 알아야됨
    # --> 1번방식.뷰 함수의 매개변수를 늘림, 2번방식.<form>로 넘어온 데이터 처리
    
    # 데이터베이스에 저장된 Bookmark 객체들 중 id변수에 저장된 값이 bookid 값과 동일한 객체를 한 개 추출 obj변수에 저장  
    obj = Bookmark.objects.get(id=bookid)
    print(obj)
    return render(request, 'bookmark/getbook.html', {'book' : obj})

###우리는 지금 
# 모델 클래스.objects.get() : 데이터베이스에 해당 모델클래스로 저장된 객체 중 특정조건을 만족하는 객체 한개를 추출하는 함수
# 모델 클래스.objects.all() : 데이터베이스에 해당 모델클래스로 저장된 모든 객체를 추출
###이거 두개만 시험해 봄.











