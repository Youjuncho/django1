from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SigninForm, SignupForm

from django.http.response import HttpResponseRedirect
from django.urls.base import reverse


# 1) 회원가입 처리 뷰
def signup(request):
    # GET, POST 구분
        # GET
        if request.method == "GET" :
            # SignupForm 객체 생성 후 HTML 파일 전달
            f = SignupForm()
            return render(request, 'cl/signup.html', {'f' : f}) # 마지막은 HTML에 보낼 객체를 사전형으로 바꾼것.
        # POST
        elif request.method == "POST" :
            # 사용자 입력 데이터 기반의 SignupForm 객체 생성
            f = SignupForm(request.POST)
            # 유효한 값이 들어있는지 확인(아이디 중복, 비밀번호 형식이 올바른지, 이메일 형식이 올바른지)
            if f.is_valid() :
                # 비밀번호 확인과 비밀번호에 들어있는 값이 같은지 확인
                if f.cleaned_data['password'] == f.cleaned_data['password_check'] :
                    # 회원 생성 # 위에 from django.contrib.auth.models import User 작성
                    # create_user(아이디, 이메일, 패스워드) : 데이터베이스에 django가 제공하는 회원 모델클래스의 객체를 생성하는 함수.
                    # 아이디, 이메일은 원본, 패스워드는 암호화된 상태로 저장됨
                    # 생성된 새로운 회원을 반환함
                    new_user = User.objects.create_user(username=f.cleaned_data['username'], email=f.cleaned_data['email'],
                                                         password=f.cleaned_data['password'])
                    # 회원정보 추가(성 - last_name, 이름 - first_name)
                    new_user.last_name = f.cleaned_data['last_name']
                    new_user.first_name = f.cleaned_data['first_name']
                    new_user.save() # 수정사항(성, 이름 변수에 값 변경)을 데이터베이스에 반영
                    print('새 유저 : ', new_user) # 새 유저 :  hycoho1996 출력
                    # 다른 URL 전송
                    return HttpResponseRedirect(reverse('vote:index'))
                    
                # 비밀번호 다른 경우
                else :
                    # HTML파일에 에러코드 전달
                    return render(request, 'cl/signup.html', {'f' : f, 'error' : '비밀번호가 같지 않습니다.'})
            # 유효한 값이 아닌 경우
            else :
                # HTML파일에 에러코드 전달
                # 에러코드가 is_valid()함수를 통과하지 못하면 User모델클래스에 설정된 에러정보가 자동으로 넘겨짐
                return render(request, 'cl/signup.html', {'f' : f})
                
from django.contrib.auth import login, authenticate, logout
# logout(request)
# 해당 요청을 한 클라이언트의 user변수를 지움

# authenticate(아이디, 비밀번호)
# 비밀번호를 암호화 한 뒤, 아이디와 암호화된 비밀번호 모두 일치하는 User 객체를 추출
# 단, 아이디나 비밀번호가 틀린 경우 None 값을 반환

# login(request, User 객체)
# 해당 요청을 한 클라이언트가 User객체의 정보를 바탕으로 로그인 처리
# 로그인이 완료된 후, request.user 변수로 해당요청을 한 클라이언트의 User객체 추출가능
# 비로그인 상태일 때는 사용할 수 있음

# 로그인 처리 과정
# 1. authenticate 함수로 로그인할 User 객체 찾기
# 2. 받은 결과가 None 값이 아닌 경우, login함수를 통해 클라이언트를 로그인 함

# 2) 로그인 처리 뷰
def signin(request):
    # GET, POST 구분
    if request.method == 'GET' :
        # SigninForm 객체 생성 후 HTML 파일 전송
        return render(request, 'cl/signin.html', {'f' : SigninForm()})
    
    # POST
    elif request.method == "POST" :
        # SigninForm 객체를 사용자 입력 기반으로 생성
        f = SigninForm(request.POST)
        # 사용자가 입력한 데이터를 추출(아이디, 패스워드)
        id = request.POST.get('username')
        # 데이터베이스에는 비밀번호를 작성했던 것이 우리가 알아볼 수 없는 암호화가 되어 저장이 된다. 하지만 pw는 우리가 작성한 비밀번호 그대로가 들어가서, authenticate을 사용 
        pw = request.POST.get('password')
        # 아이디랑 패스워드가 일치하는 User 모델클래스 객체 추출
        # u : 회원이 있는 경우 User객체, 없는 경우 None 값이 저장됨. 
        u = authenticate(username = id, password = pw)
        # 회원이 있는 경우
        if u :
            # 로그인 처리
            login(request, u)
            nexturl = request.POST.get('nexturl')
            # nexturl : 이동할 URL주소가 있는 경우 메인페이지로 가지 않고 저장된 URL로 리다이렉트
            if nexturl :
                return HttpResponseRedirect(nexturl)
            else :
                return HttpResponseRedirect(reverse('vote:index'))
        # 회원이 없는 경우
        else :
            # 아이디 or 비밀번호 틀렸다는 에러코드 전달
            return render(request, 'cl/signin.html', {'f' : f, 'error' : '아이디나 비밀번호가 틀렸습니다.'})

# 3) 로그아웃 처리 뷰
def signout(request):
    # 요청한 클라이언트가 로그아웃
    logout(request)
    # 다른 URL 전송
    return HttpResponseRedirect(reverse ('cl:signin'))


