from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index_view,name='index'),
    #path of login
    #templates/login
    path('login/',views.login_view,name='login'),
    path('signup/', views.signup_view,name='signup'),
    path('about/', views.about_view,name='about'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)