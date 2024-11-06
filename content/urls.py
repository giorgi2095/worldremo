from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from content import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='loginUser'),
    path('register', views.RegisterUser, name='registerUser'),
    path('logout', views.logoutUser, name='logoutUser'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)