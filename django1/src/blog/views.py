from django.shortcuts import render

# 제네릭뷰 : 장고에서 제공하는 여러가지 뷰 기능을 구현한 클래스
# ListView : 특정 모델클래스의 객체 목록을 다루는 기능이 구현된 뷰
# DetailView : 특정 모델클래스의 객체 1개를 다루는 기능이 구현
# FormView : 특정 폼클래스를 다루는 기능이 구현
from django.views.generic.detail import DetailView

from django.views.generic.list import ListView
from pyexpat import model
from blog.models import Post, PostFile, PostImage
from blog.forms import PostForm
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

# 1) index : 글목록이 뜨는 메인페이지
class Index(ListView):
    # 해당 뷰가 사용할 html 파일의 경로
    template_name = 'blog/index.html'
    # 리스트로 뽑을 모델클래스
    model = Post
    # 템플릿에게 객체리스트를 넘겨줄 때 사용할 키 값 
    context_object_name = 'list'
    # 한 페이지에 최대 몇개의 객체가 보여질지 설정
    paginate_by = 5

# 2) detail : 글 상세보기 페이지
class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'obj'

# 3) posting : 글쓰기 페이지
class Posting(LoginRequiredMixin,FormView): # qregister함수의 처음부터 ~ 113까지 FormView로 가져왔다.
    template_name = 'blog/posting.html'
    # 연동할 폼클래스 저장
    form_class = PostForm
    # is_valid()함수가 True를 반환한 뒤의 처리를 form_valid()함수를 오버라이딩해서 작성
    def form_valid(self, form):
        # 매개변수 form : is_valid()함수를 통과한 PostForm 객체
        # PostForm객체를 바탕으로 Post객체 저장
        # 글쓴이(author) 변수가 비어있으므로, 데이터베이스에 저장하지 않음
        
        p = form.save(commit = False) # p : Post객체
        # request.user : 요청한 클라이언트의 로그인정보(User 모델클래스 객체)
        p.author = self.request.user # 로그인을 한 사람과 작성자를 매칭
        p.save() # Post 객체가 데이터베이스에 저장됨
        
        # 클라이언트가 보낸 첨부파일, 이미지파일을 바탕으로 PostFile, PostImage객체 생성 및 저장
        # request.FILES : 클라이언트가 서버로 보낸 파일정보를 관리하는 변수
        # return FormView.form_valid(self, form)
        
        # PostFile 객체를 생성
        for f in self.request.FILES.getlist('files') : # 파일을 몇개를 보낼지 모르기때문에 for문을 이용해서 하나씩 꺼냄(?)
            # f : 파일 정보
            pf = PostFile() # 새로운 PostFile 모델클래스의 객체 생성 # models에서 PostFile로 입력양식을 제공을 했기 때문에
            pf.file = f
            pf.post = p 
            pf.save() # 데이터베이스에 새로운 PostFile 객체가 처장됨
        
        # PostImage 객체를 생성
        for i in self.request.FILES.getlist('images') : # getlist도 파일이나 이미지가 몇개일지 모르기 때문에 사용
            # i : 이미지 정보
            pi = PostImage()
            pi.post = p
            pi.image = i
            pi.save()
        
        # 완성된 글페이지로 URL이동
        return HttpResponseRedirect( reverse('blog:detail', args=(p.id,)))
    
            
    
    