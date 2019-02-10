# 만들어진 모델클래스와 템플릿을 이용해서 어떤 데이터로직을 하는 곳이 view!
from django.shortcuts import render, get_object_or_404
# get_object_or_404 : 특정한 모델클래스에 id값을 조건으로 검색해 객체 추출.(get함수 사용)
# 단, 객체가 존재하지 않는 경우에 웹 클라이언트의 요청이 잘못된 것으로 판단해 더이상 뷰함수가 진행되지 않고 404에러페이지를 클라이언트에게 전달
from .models import Question, Choice # 같은 파일에 있는 models.py의 Question모델클래스를 임포트하겠다.
# reverse(별칭문자열, args=(매개변수값)) : 별칭기반으로 URL주소 반환. 127.0.~ 이렇게 써도 되지만, reverse를 이용해서 별칭으로 쓰겠다.
# HttpResponseRedirect(url주소문자열) : 해당 URL주소를 클라이언트에게 전달
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect

# 1) 질문 리스트(index)
def index(request):
    # 모든 Question 객체 추출
    #( 슬라이싱 : iterable 데이터의 특정 범위 만큼의 요소를 추출하는 방식
    # ex) a = [1,2,3,4,5]
    # a[1:4] --> [2,3,4] 추출
    # 시작인덱스가 빈칸인 경우 --> 0번 인덱스부터 추출
    # 종료인덱스가 빈칸인 경우 --> 마지막 인덱스의 요소까지 추출
    # 인덱스 값이 음수인 경우 --> 맨 뒤  요소부터 인덱스를 찾음 )
    qlist = Question.objects.all()# [-3:] # qlist는 내가 만들어준 변수
    
    # 추출한 객체를 HTML에 전달 및 클라이언트에게 HTML 전달
    return render(request, 'vote/index.html', {'objs' : qlist}) # vote/index.html에서 폴더이름 vote가 왜 중복되면 안되는지 설명!!그 bookmark먼저 순서대로 찾고~이런거

# 2) 질문 선택 시 답변항목 제공(detail)
def detail(request, q_id):
    # 1. q_id 값을 이용해 Question 객체 한 개 추출
    # get_object_or_404(모델클래스명, 조건)
    q = get_object_or_404(Question, id = q_id)
    # 2. Question객체와 연결된 모든 Choice객체 추출
    # 모델클래스A의 객체.모델클래스B_set : A모델클래스와 B모델클래스가 1:n관계인 경우, 해당 A객체와 연결된 B객체들을 대상으로 get(), all(), filter(), exclude()함수들을 사용할 수 있다.
    # q.choice_set : 해당 Question객체와 연결된 choice객체들을 대상으로 선정 (여기서 q는 아까 models.py에서 외래키 지정했을 때 사용했던 변수이다.)
    ### 아까 model.py에서 q를 쓴 것 --> choice가 연결된 Question을 찾으려는?그런거고(살짝 주동)
    ### 지금 q.choice_set을 쓴 것 --> Question에서 아까 연결당했던(?) Choice를 찾으려고 사용(살짝 수동) 즉, 관계에서 1에 해당하는 객체가 n을 가져올 때 사용
    c_list = q.choice_set.all()
    # 결과로 HTML 파일 전달
    return render(request, 'vote/detail.html', {'q' : q, 'c_list' : c_list})

# 3) 웹 클라이언트가 선택한 답변항목의 투표수를 늘리는 처리(vote)
def vote(request):
    # POST방식으로 사용자가 요청했는지 확인
    # --> HTML의 form태그의 요청방식을 POST로 했기 때문에 
    # request.method : 사용자의 요청방식이 문자열형태로 저장된 변수. 대소문자 구분이 있으므로 사용시 "GET", "POST"로 비교
    if request.method == "POST" : # request의 method를 사용하겠다! 처음으로 request를 사용
        # request.POST : 클라이언트가 POST방식으로 요청할 때 넘어온 데이터가 저장된 변수
        # request.GET : 클라이언트가 GET 방식으로 요청할 때 넘어온 데이터가 저장변수
        # 사전형데이터.get(키값) : 사전형 데이터에서 키값에 해당하는 값을 추출하는 함수
        c_id = request.POST.get('a') # a인 이유는 detail.html에서 name을 a로 해서 키값을 주었기 때문.
        # c_id와 같은 id변수값을 가진 Choice객체를 추출
        c = get_object_or_404(Choice, id=c_id)
        # 해당 Choice객체의 votes 변수값에 1을 누적
        c.votes += 1 # votes = models.IntegerField(default = 0) # 투표수 저장을 위해 (models.html에서 votes로 줬기 때문에)
        c.save() # 해당 객채의 변수값 변동을 데이터베이스에 반영
        # 투표결과 화면을 보여준다.
        # ppt에서 58번에 vote()꺽이는 선 --> 투표수를 늘리는 처리를 화면으로 이동을 하는것이 아니기 때문이다.
        return HttpResponseRedirect(reverse('vote:result', args=(c.q.id,))) # 여기서 q는 model.py에서 Question을 연결하는 매개변수이다.
        
      
# 4) 웹 클라이언트가 선택한 질문의 답변 투표결과(result)
def result(request, q_id):
    # Question객체를 찾기
    q = get_object_or_404(Question, id=q_id)
    # 결과 HTML 클라이언트 전송
    return render(request, 'vote/result.html', {'q' : q})

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 데코레이터 : URL Conf를 통해 View함수가 호출될 때, 뷰가 실행되기 전 먼저 실행되는 함수.
# 뷰함수에만 데코레이터를 적용할 수 있다.
# 뷰클래스는 XXXMixin 클래스를 상속받아 데코레이터로 처리
# 데코레이터 적용 방식
# @데코레이터 함수 이름
# def 뷰함수(request) :

# 클래스에 데코레이터 적용 방식
# class 뷰클래스(XXXMixin) : 

# login_required : 뷰함수 호출 전 요청을 한 클라이언트가 비로그인 상태인 경우, 웹프로젝트에 지정된 로그인 URL로 넘어가는 데코레이터 함수

# 로그인 URL 지정방법
# settings.py --> LOGIN_URL 변수에 URL 저장

from django.contrib.auth.decorators import login_required


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

from .forms import QuestionForm, ChoiceForm
from _datetime import datetime

# 1) Question 객체를 사용자가 등록하는 뷰
# '질문추가' 링크를 타고 온 클라이언트에게는 비어있는 QuestionForm 기반의 입력양식을 제공 (GET방식)
# 추가한 뒤, 폼을 제출한 경우 --> 클라이언트가 작성한 정보를 바탕으로 Question객체를 생성 및 DB에 저장 (POST방식)
# --> 완성된 객체에 대한 detail 뷰 호출
@login_required
def qregister(request):
    # 사용자의 요청방식을 구분해 처리
    # 사용자 요청이 GET 방식일 때의 처리
    if request.method == "GET" :
        # QuestionForm객체를 생성
        # 모델클래스 객체 생성 시 매개변수에 아무런 값도 전달하지 않는 경우, 입력양식에 값이 비어있는 형태로 객체가 생성된다.(관리자창에서 q, name등이 빈칸으로)
        f = QuestionForm()# 따라서 일부러 비워놓은것.
        # HTML 파일에 폼객체 전달
        return render(request, 'vote/qregister.html', {'f' : f})
    
    # 사용자 요청이 POST 방실일 때의 처리
    elif request.method == "POST" :
        # 1. 사용자가 보낸 데이터를 기반으로 QuestionForm 객체 생성
        # request.POST : POST 방식으로 요청했을 때 동봉된 데이터(사전형)
        f = QuestionForm(request.POST) # POST방식으로 돌아온 객체만 QuestionForm객체를 생성해서 f라는 변수에 대입. 즉, name변수만 request.POST로 받아들여서 저장
        
        # 2.사용자가 보낸 데이터가 유효한 값인지 확인
        if f.is_valid() :
            # 폼객체.is_valid() : 사용자 입력이 유효한 값인 경우 True, 유효하지 않는 값이 입력되면 False 반환
            # 폼객체.is_valid() 결과로 True가 반환된 경우, 폼객체에 들어있는 각 데이터들을 추출할 수 있다. --> 폼객체.cleanded_data 변수 사용 가능
            # ex) QuestionForm 객체.cleaned_data['name'] 사용 가능
            print('cleaned_data["name"]', f.cleaned_data['name']) # 작업 관리창이랑 비교 detail로 넘어간 화면에서 비교
            
            # 3. 모델폼객체(QeustionForm) 기반으로 모델객체(Question)객체 생성
            ###호오오오옥시 사용자가 작성한 POST방식으로 보낸 것이 Question객체 즉, name,date등을 사용하여 나타내지기 위해 QuestionForm을 기반으로 Question객체를 생성하는 것인가?
            # 모델폼객체.save() : 연동된 모델클래스의 객체로 변환 및 반환, 데이터베이스 저장
            # QuestionForm으로 Question 객체 저장 시, date변수에 값이 없어 데이터베이스에 저장 시 에러가 발생
            # 따라서 QuestionForm을 기반으로 Q객체를 생성해야 하는데, date변수가 입력이 안되는 것이 문제가 되지 않도록 데이터베이스에는 저장하지 않고, 변환만 하는 것.
            # 모델폼객체.save(commit=False) : 연동된 모델클래스의 객체로 변환 및 반환(q에 넣어줌)
            q = f.save(commit=False)
            
            # 4. 값이 비어있는 date 변수에 값 채우기
            q.date = datetime.now() # 현재 컴퓨터의 날짜/시간정보를 date변수에 저장
            # 확인차
            print('데이터베이스에 저장되기 전 Question 객체의 id 값', q.id) # 데이터베이스에 저장되기 전 Question 객체의 id 값 None 출력
            
            # 5. 데이터베이스에 저장
            q.save()
            # 확인차
            print('데이터베이스에 저장된 후 id값', q.id) # 데이터베이스에 저장된 후 id값 5 출력
            
            # 6. 새로 생성된 객체의 id값을 통해 detail 뷰 호출 --> detail.html를 호출하는게 아니라, 위에 detail 뷰를 호출해서 이어져 있는 detail.html의 화면으로 넘어가는 것이다.
            return HttpResponseRedirect(reverse('vote:detail', args=(q.id,)))
        
            '''
            즉, 정리를 하면  질문생성 링크를 타고 들어가면 사용자의 요청이 GET방식이 된다.
      GET방식일 경우에는 QeustionForm 객체를 생성하고 , QuestionForm은 이미 forms에서 Question의 객체를 사용한다고 
            선언을 했기 때문에  f라는 변수에 넣어주고, 그대로 qregister.html 주소로 리턴을 해주면, 실제로 질문생성을 할 수 있는 
            화면을 제공해 준다.
            사용자가 새로 생성할 질문을 작성하고 난 뒤, POST방식으로 보내면  request.POST을 통해 POST방식으로 돌아온 객체를 
      QuestionForm 객체를 생성해서 f라는 변수에 대입. 사용자가 보낸 값이 유효한지 검사를 하고, 
      QuestionForm 폼객체를 기반으로 Question 객체를 생성해주고(=q), 모델폼객체.save(commit=false)를 통해 연동된 모델클래스의 객체로 변환. --> Question객체를 생성한 이유가 date변수에 값이 없어서 인가?
           그런 다음 Question객체로 (name, date) 값을 변환해 준 것을 데이터베이스에 저장하고, vote의 detail뷰함수로 호출.'''
        '''
        질문을 생성하고 detail.html화면으로 넘어가도 radio가 없는 이유는 아직 Choice를 만들어 주지 않았기 때문이다. 
        질문 생성(=name)과 날짜와 시간(=date)만 보여준다. 
    GET방식으로 보낸 QuestionForm()에 사용자가 작성한 것을 POST방식으로 다시 받아들일 때, QuestionForm(request.POST)로 받아들인 것이고,
        받아들인 값이 유효할 경우에만, cleaned_data를 이용해서 사용자가 작성한 값을 받아 들인다. 
        이 받아 들인 결과값을 화면으로 보여주기 위해서 Questionform객체를 기반으로 Question객체로 변환.
    date의 값도 넣어준 다음, 데이터베이스에 저장. 그리고 detail뷰함수로 호출 --> detail뷰함수에서 구성하는 detail.html화면으로 자동 구성
       '''
            
# 2) Question 객체를 사용자가 수정하는 뷰
@login_required
def qupdate(request, q_id): # q_id매개변수를 추가해 준 이유는 많은 질문들 중 사용자가 수정하고자 하는 질문을 찾아야 하기 때문
    # 수정하고자 하는 객체를 추출
    q = get_object_or_404(Question, id = q_id)
    # GET, POST 방식 분류
    # GET 방식인 경우
    if request.method == "GET" :
        # 데이터베이스에 저장된 객체를 기반으로 QeustionForm 객체를 생성 --> q : 데이터베이스에 저장된 객체
        # HTML 코드로 변환 시 빈칸이 아닌 해당 객체에 저장된 값으로 채워진 형태로 변환 됨
        f = QuestionForm(instance = q) # instance는 object와 똑같다고 보면 된다. object는 객체라는 의미. 즉, 위에 지정해준 q의 객체를 쓰겠다.
        # 생성된 QuestionForm 객체를 HTML에 전달 및 전송
        # qregister.html과 유사하게 HTML코드가 구현되기 때문에 기존에 만들어진 HTML파일을 재사용. form태그의 action 속성을 빈칸으로 처리했기 때문에,
        # qregister 뷰에서 qregister.html를 쓴 것과, qupdate 뷰에서 qregister.html를 쓴 결과가 각자의 뷰함수로 POST요청을 함.
        return render(request, 'vote/qregister.html', {'f':f})
        

    # detail뷰함수에서 넘어가는 detial.html의 action은 vote:vote로 했기 때문에, vote뷰함수로 POST요청을 하는 것이다.
    # qregister.html의 action은 "" 빈칸으로 비워두었기 때문에, qupdate함수의 GET방식에서 qregister.html을 사용하면 qregister.html에서 사용자가 작성한 것이 qupdate뷰함수에서 POST요청을 받아들이고,
    # qregister뷰함수에서 사용하면 qregister.html에서 쓴 결과가 qregister의 뷰함수로 POST요청을 하는 것이다.
    # 즉, action이 빈칸이어서 qregister.html을 작성한 뷰 함수의 POST로 넘어온다.
    
    # POST 방식인 경우
    elif request.method == 'POST' :
        # 데이터베이스에 저장된 객체 + 사용자의 입력데이터를 기반으로 QuestionForm 객체 생성
        f = QuestionForm(request.POST, instance = q) # 사용자가 수정한 내용 : request.POST + 기존에 있던 내용 : instance = q --> q객체로 사용자가 수정한 내용을 QuestionForm객체를 생성하겠다.
        # 유효한 값이 들어있는지 확인
        if f.is_valid() :
            # 데이터베이스에 저장
            # 덮어씌우는 것은 name 하나이기 떄문에 date를 수정해 줄 필요가 없다. 따라서 commit 이런거 안해도된다.
            qu = f.save() # qu는 내가 만들어준 것. 아래 print를 확인해보기 위해 qu 변수에 넣어주었다.
            print('사용자 요청으로 찾은 객체 : ', q) # 사용자 요청으로 찾은 객체 :  qregister로 생성된 객체 수정
            print('값이 수정된 객체 : ', qu) # 값이 수정된 객체 :  qregister로 생성된 객체 수정 출력
            # 이동할 URL주소 클라이언트에게 전달
            return HttpResponseRedirect(reverse('vote:detail', args=(q.id,)))
    
# 3) Question 객체 삭제
@login_required
def qdelete(request, q_id):
    # 삭제할 Question 객체 추출
    q = get_object_or_404(Question, id = q_id)
    # 삭제 함수 호출
    print('데이터베이스에 삭제되기 전 id변수 :', q.id) # 데이터베이스에 삭제되기 전 id변수 : 6 출력
    # 해당 객체를 데이터베이스에서 삭제함. 삭제한 객체에 저장된 변수값은 사용할 수 있다.
    q.delete()
    print('삭제된 후 id 변수 값 :', q.id) # 삭제된 후 id 변수 값 : None
    # 다른 URL or HTML 파일 전달
    return HttpResponseRedirect(reverse('vote:index'))
    
#4) Choice 객체 등록
@login_required
def cregister(request):
    # 사용자 요청방식 구분 (GET, POST) request.method
    if request.method == "GET" :
        f = ChoiceForm() 
        # f.as_p(), f.as_table(), f.as_ul()
        # --> HTML 코드 형태로 변환하는 함수
        print('f.as_table()에서 반환하는 값 : ', f.as_table()) # 확인 (위에 Q에서는 원래 HTML 파일에서 줬는데, 여기서 주는 새로운 시도를 함)
        # f.as_table()에서 반환하는 값 :  <tr><th><label for="id_q">Q:</label></th><td><select name="q" required id="id_q"> 출력
        return render(request, 'vote/cform.html', {'i' : f.as_table()})# 오는 대상, 보낼 HTML파일 주소, 사전형형태로 html파일 인자 값을 넘겨주어라. 
   
    elif request.method == "POST" :
        # 사용자 입력기반 ChoiceForm객체 생성, 유효값 확인, Choice객체 변환 및 저장
        f = ChoiceForm(data = request.POST) # data는 순서가 헷갈리지 않게 그냥 넣어줌. f = ChoiceForm(request.POST)와 똑같음
        if f.is_valid(): # 사용자 입력이 유효한 값일 때의 처리
            # 사용자 입력으로 Choice 객체에 변수들의 값이 채워진 상태이므로, 바로 데이터베이스에 저장해도 됨.
            c = f.save() # c : 사용자 입력기반의 새로운 Choice 객체
            # c.q.id : Choice 객체가 연결한 Question객체의 id 값 
            return HttpResponseRedirect(reverse('vote:detail', args =(c.q.id,)))# args--> 위에 detail함수에서 (request,q_id)로 추가적인 매개변수 :q_id가 있기 떄문에 args(c.q.id)를 해줘야 id값도 보여줄 수 있다.
        else : # 사용자 입력이 유효하지 않는 값일 때의 처리
            # f : 사용자가 입력한 데이터를 바탕으로 생성된 form 객체이다.
            # --> 입력공간이 빈칸이 아니라 사용자 입력으로 채워져 있으며, 화면을 그대로 보여주기 위해 HTML파일을 그대로 작성하고 추가적으로 error메세지도 같이 넣어준 것이다. ex) 네이버 로그인 틀릴 시 화면
            return render(request, 'vote/cform.html', {'i' : f.as_table(), 'error' : '잘못된 입력입니다.'})

#5) Choice 객체 수정
@login_required
def cupdate(request, c_id):
    # 수정할 Choice 객체 추출
    c = get_object_or_404(Choice, id = c_id) # 어떤 모델클래스에서 할 것인지, 어떤 값을 추출할 것인지
    # GET, POST 분리
    if request.method == "GET" :
        # ChoiceForm객체 생성 - Choice객체 기반
        f = ChoiceForm(instance = c)
        # HTML 전달
        return render(request, 'vote/cform.html', {'i' : f.as_table()}) # 보낼 대상, 보낼 HTML파일주소
    # POST
    elif request.method == "POST" :
        # ChoiceForm 객체 생성 - Choice객체 + 사용자입력
        f = ChoiceForm(request.POST, instance = c) # 여기서 c는 위에 수정할 객체추출에서 정한 변수 c
        # 유효한 값인지 확인
        if f.is_valid() :
            # 데이터베이스에 수정사항 반영
            f.save() # c변수와 f.save()함수에서 주는 Choice객체가 동일하기 때문에 변수에 저장하지 않음.
            # 다른 URL을 사용자에게 전송
            return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))

#6) Choice 객체 삭제
@login_required
def cdelete(request, c_id):
    c = get_object_or_404(Choice, id = c_id)
    c.delete()
    return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))















    
