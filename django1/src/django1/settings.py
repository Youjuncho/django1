"""
Django settings for django1 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from django.urls.base import reverse_lazy
# reverse_lazy와 reverse의 공통점
# --> 등록된 URL의 별칭을 바탕으로 URL을 반환하는 함수
# 차이점
# --> URL을 반환하는 시기
# reverse : 함수 호출이 되자마자 등록된 URL에서 찾음
# reverse_lazy : 웹서버가 정상적으로 실행이 된 뒤에 등록된 URL에서 찾음

# 헷갈리는 경우 모든 파이썬코드에서 reverse_lazy를 써도 무방함.

# login_required 데코레이터가 띄우는 로그인 URL을 설정
LOGIN_URL = reverse_lazy('cl:signin')
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ###
# 소셜로그인 완료 후 이동할 URL주소를 저장하는 변수 - DJANGO의 기본으로 깔려있는 기능이다.
LOGIN_REDIRECT_URL = reverse_lazy('blog:index')

# social_django 어플리케이션의 설정값

# 2) 인증관련 모듈을 추가
AUTHENTICATION_BACKENDS = (
    # 구글 로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId', # 구글에서 가져오겠다.
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    # 소셜로그인 정보를 django의 User 모델클래스에 저장하기 위한 클래스
    'django.contrib.auth.backends.ModelBackend'
    )

# 4) 구글 개발자 사이트에서 발급받은 ID, PASSWORD 저장
SOCIAL_AUTH_GOOGLE_PLUS_KEY =  '824140580964-0fue25n09t6jjuq3pm0s8tv7nheav38m.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = 'uE4xIvc9szEIrlIwJADC5oty'
### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ###

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r1a)f7ugr8(fa0s(godzq(9!o_(ao$8ter8s$+lxwe#7d*643j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 프로젝트 내에서 실행할 어플리케이션을 등록/관리하는 변수 (즉, 자주 바꿔줄것이다.)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark', # 웹 프로젝트에 bookmark 어플리케이션이 존재하는 것을 등록
    'vote',
    'customlogin',
    'blog',
    # 1) pip install social-auth-app-django 명령어로 모듈이 설치되있어야 사용 가능하다.
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ###
                # 3) 소셜로그인 처리를 위한 템플릿 관련 함수 추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                ### ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ###
            ],
        },
    },
]

WSGI_APPLICATION = 'django1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 클라이언트의 요청으로 저장하는 미디어파일(이미지, 첨부파일) 설정
# MEDIA_URL : URL주소로 파일 주소를 접근할 때 사용하는 URL을 저장하는 변수
# 127.0.0.1:8000/files/로 시작하는 경로는 미디어파일을 불러오는 것으로 판단한다.
MEDIA_URL = '/files/'

# MEDIA_ROOT : 실제 파일이 저장되는 하드웨어 경로
# BASE_DIR : 웹프로젝트가 저장된 경로
# os.path.join(기존경로, 새경로) : 기존경로에 새경로를 붙인 문자열을 생성

# 현재 프로젝트 폴더/files에 클라이언트가 업로드한 파일이 저장되도록 설정
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
# C:/files/폴더에 미디어파일이 저장되도록 설정
# MEDIA_ROOT = 'c:/files' 

# MEDIA_URL과 MEDIA_ROOT를 설정한 뒤, 메인 URLConf에서 URL과 하드웨어 경로를 매칭하는 작업을 수행해야 한다.


