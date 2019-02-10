from .models import Post
from django import forms

# 글쓰기에 사용할 폼클래스 - 모델폼클래스 상속
class PostForm(forms.ModelForm):
    # 사용자가 첨부파일, 이미지를 업로드할 수 있도록 커스텀 입력양식 생성
    # required=False : 해당 <input>을 사용자가 필수로 입력하지 않아도 되는 설정. 즉, 이미지랑 파일을 꼭 하나 이상 업로드 하지 않아도 오류가 뜨지 않도록 하는것.
    # 첨부파일을 업로드하지 않아도 되는 설정
    # ClearableFileInput : <input type = 'file'> 형태의 입력공간에 파일 관련 추가 설정을 할 수 있는 위젯 (javascript나 css를 배우지 않았다는 가정하에 사용한 것)
    # multiple : 하나의 입력공간에 여러개의 파일을 업로드할 수 있도록 허용
    files = forms.FileField(required = False, widget = forms.ClearableFileInput(attrs={'multiple':True}))
    
    images = forms.ImageField(required = False, widget = forms.ClearableFileInput(attrs={'multiple':True}))
     
    class Meta : 
        model = Post
        fields = ['category', 'headline', 'content'] # 사용자가 작성할 것들만 fields로 가져옴.