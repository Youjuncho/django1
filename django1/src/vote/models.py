from django.db import models

# 질문
# 질문제목 생성일
class Question(models.Model):
    # qr페이지에서 사용자에게 name으로 뜨기 때문에, 한글로 나올 수 있도록 앞에 ''를 통해 별칭을 넣어준다.
    # foriegnKey(외래키)는 바꿀 수 없다.
    name = models.CharField('질문제목', max_length = 100)
    # DateField : 날짜(년원일) 데이터만 저장하는 공간
    # DateTimeField : 날짜 + 시간을 저장하는 공간
    date = models.DateTimeField('생성일')
    def __str__(self):
        return self.name
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
class Meta : # 모델클래스에 정의된 변수, 테이블 이름 등을 처리할 때 사용하는 클래스.
    # ordering : 해당 모델클래스에 정의된 변수 중에서 정렬에 사용할 변수 이름을 저장하는 변수(Question에서는 name, date, 자동으로 주어지는 id변수 3가지가 해당)
    # 변수이름만 쓴 경우 --> 오름차순, -변수이름 쓴 경우 --> 내림차순
    ordering = ['-date'] # 가장 최근에 만들어진 객체 순으로 정렬
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 답변
# 어떤 질문에 연결되있는지 답변내용, 투표수도 저장을 해줘야 한다.
class Choice(models.Model):
    # ForeignKey(연결할 다른 모델 클래스) : ForeignKey 객체를 만든 모델클래스의 객체들이 연결한 모델클래스의 객체와 1:n 관계로 연결할 수 있는 설정
    # 즉, choice모델클래스의 foreignkey를 통해 n이 되고 싶은 입장에서  1:n 관계를 설정
    # Foreignkey의 객체를 저장한 변수는 연결한 모델클래스의 객체를 저장하는 변수가 된다.
    # Choice객체.q.name --> 해당하는 Choice객체와 연결된 Question객체의 name변수값을 추출 (즉, Question의 변수 name,date를 쓰겠다는것.)
    # on_delete : 연결된 모델클래스의 객체가 삭제될 때 어떻게 처리할지 지정하는 변수
    # on_delete = models.PROTECT : 연결된 모델클래스의 객체가 삭제되지 않도록 막아주는 기능
    ###즉, 여러개의 Question객체가 있는데, 그에 따른 choice(답변)객체가 하나라도 있을 경우에는 Question객체가 삭제되어도 같이 삭제되지 않도록 막아주는 것이다.
    # models.CASCADE : 연결된 모델클래스의 객체가 삭제되면 같이 삭제됨
    # models.SET_NULL : 연결된 모델클래스의 객체가 삭제되면 아무것도 연결되지 않은 상태로 유지(즉, Q가 삭제되어도 C는 남아있음)
    # models.SET(연결할객체) : 연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
    # models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 설정된 객체와 연결
    # 위에 총 5가지를 on_delete에 선택해서 넣을 수 있다.
    q = models.ForeignKey(Question, on_delete = models.CASCADE) # Question모델클래스와 1:n 관계를 가지는데 위에 주석대로 choice모델클래스의 외래키가 n이 되도록 설정. n에 해당하는 곳에 외래키를 작성
    name = models.CharField('답변항목',max_length = 50)
    # IntegerField : 정수값을 저장하는 공간
    # default : 모델클래스의 객체 생성시 해당 저장공간에 기본값 설정
    # default는 모든 Field에서 사용할 수 있다. 
    votes = models.IntegerField('투표수', default = 0) # 투표수 저장을 위해
    
    def __str__(self):
        return self.q.name + '/' + self.name
        #self.q.name은 C와 연결된 Q에서 사용하는 객체name을 가져온것 + self.name은 C에서 사용하는 객체name
    