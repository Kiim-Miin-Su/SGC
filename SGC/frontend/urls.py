from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('lessons/', views.lessons, name='lessons'),
    path('human_resources/', views.human_resources, name='human_resources'),
    path('community/', views.community, name='community'),
    path('used_instruments/', views.used_instruments, name='used_instruments'),

    # 로그인/로그아웃
    path('log_in/', auth_views.LoginView.as_view(template_name='log_in.html'), name='log_in'),
    path('log_out/', auth_views.LogoutView.as_view(next_page='/'), name='log_out'),

    # 회원가입
    path('sign_up/', views.signup, name='sign_up'),
    
    # 강좌 관련 URL
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/enroll/', views.enroll_lesson, name='enroll_lesson'),
    path('my_page/', views.my_page, name='my_page'),
    path('classroom/<int:lesson_id>/', views.enter_classroom, name='enter_classroom'),
]
