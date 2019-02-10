# form : HTML의 <form>태그에 들어가는 <input>태그들을 관리하는 클래스/기능
#        모델클래스에 저장된 변수들에 맞춰 자동설정도 할 수 있으며, 커스텀입력공간(비밀전호 확인)도 생성할 수 있다.

# class 클래스명(ModelForm 또는 Form) :
# ModelForm : 모델클래스를 기반으로 입력양식을 자동 생성할 때 상속받는 클래스 -->우리는 이걸 사용
# Form : 커스텀 입력양식을 생성할 때 상속받는 클래스
# ModelForm을 상속받았을 때도 커스텀 입력양식을 생성할 수 있다.

# 폼 클래스의 객체를 함수를 통해 HTML문서의 코드로 변환할 수 있다. (<p>, <table>, <li>)
#    ex1) 폼클래스객체.as_p() --> 해당 폼 객체에 저장된 입력공간들을 <input>태그로 변환하고, 개별적으로 <p>태그로 묶은 문자열을 반환.
#    ex2) 회원가입폼클래스객체.as_p() --> p로 변환한 경우의 예
#    '''<p> <label>아이디</label> <input type = "" name = ""></p>
#        <p> <label>비밀번호</label> <input type = "" name = ""></p>''' 문자열 반환

# 폼 설정 순서
# 1) ModelForm/Form 클래스 임포트
# 2) 사용할 모델클래스 임포트 --> (Question,Choice)
# 3) ModelForm/Form 클래스를 상속받은 폼클래스 정의

# 만들어진 폼클래스는 view에서 객체 생성을 통해 활용한다.

# 기존 개발 순서 (혼자서 할때)
# 어플리케이션 생성 --> settings.py 등록 --> 모델 정의 --> 데이터베이스 반영 --> 뷰 정의 --> 템플릿 정의 --> URLConf 등록
# (form)개발 순서 변경
# 어플리케이션 생성 --> settings.py 등록 --> 모델 정의 --> 데이터베이스 반영 --> 폼클래스 정의 --> 뷰 정의 --> 템플릿 정의 --> URLConf 등록


from django.forms.models import ModelForm # 1)에 해당
from .models import Question, Choice # 2)에 해당, 현재 같은 위치에 있기 때문에 Q와 C를 사용하기 위해서는 임포트

# 3)에 해당
class QuestionForm(ModelForm) :
    class Meta : # Meta클래스 : 연동하고자 하는 모델클래스에 대한 정보를 정의하는 클래스 
        # Meta 안에서 사용할 수 있는 변수 3가지.
        # 1. Model : 연동하고자 하는 모델클래스를 저장하는 변수
        # 2. fields : 모델클래스에 정의된 변수 중 어떤 변수를 클라이언트가 작성할 수 있도록 입력양식으로 제공할 것인지 지정하는 변수(iterable - list, tuple타입)
        # 3. exclude : 모델클래스에 정의된 변수 중 입력양식으로 만들지 않을 것을 지정하는 변수(list타입)
        # 즉, 변수 중 사용하고 싶은 것만 고르는 변수 --> fields / 사용하지 않는 것을 고르는 변수 --> exclude
        model = Question # Q클래스를 연동해서 Q클래스의 변수를 사용하겠다. name과 date가 있다.
        fields = ['name'] # name변수만 입력할 수 있는 form 생성
        # exclude = ['date'] # date변수를 제외한 모든 변수를 입력할 수 있는 form 생성

class ChoiceForm(ModelForm):
    class Meta :
        model = Choice
        exclude = ['votes'] 
        # fiedls = ['q', 'name']
        # fields = ('q', 'name')
        
