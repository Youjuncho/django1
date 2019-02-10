
# django에서 제공하는 auth 어플리케이션의 models.py 임포트
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms # d:디장고 폴더 안에 있는 forms 자체를 임포트 -*

# 1) 회원가입에 사용할 모델 폼 클래스
class SignupForm(ModelForm):
    # 생성자 오버라이딩 - password_check 변수의 label 수정
    def  __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 상속받은 클래스의 생성자 호출
        # password_check 변수의 label 속성 수정
        self.fields['password_check'].label = "비밀번호 확인"
    
    # 모델클래스에 없는 입력양식을 생성 - 커스텀 입력양식 (User모델클래스에는 <비밀번호 확인>이 없기 때문에, 나와서 새로 작성)을 위해 위에 -*을 작성
    # forms에 들어있는 XXXXField 클래스의 객체를 클래스변수에 저장해 커스텀입력양식을 생성할 수 있다.
    # 모델클래스의 저장공간을 생성하는 것과 유사하나 서로 다른 기능을 만들 때 사용함
   
    # forms에 들어있는 XXXXInput 클래스의 객체를 widget으로 지정하면 해당 타입으로 입력양식이 생성됨.

    # 비밀번호 확인 --> 비밀번호 타입으로 변경
    password_check = forms.CharField(max_length=200, widget = forms.PasswordInput())
    # 객체 생성을 위해 forms.passwordInput에 괄호도 넣어줌 ()
    
    # <input>의 순서를 지정
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']
    
    class Meta :
        model = User # User 모델클래스를 연동하겠다.
        widgets = {
            # '비밀번호'도 비밀번호 타입으로 변경
            'password' : forms.PasswordInput()
            }
        # ID, 비밀번호, 성, 이름, 이메일
        # User모델클래스에 무슨 변수가 있는지 모르기 때문에, ctrl을 눌러서 확인해봐야한다. 시간관계상 그냥 알려줘서 작성.
        fields = ['username', 'password', 'last_name', 'first_name', 'email']

# 2) 로그인에 사용할 모델 폼 클래스
class SigninForm(ModelForm):
    class Meta :
        model = User
        fields = ['username', 'password']










