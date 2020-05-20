from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index, name="index_page"),
   path('submit/', views.submit, name="submit_page"),
   path('login', views.login, name="login_page"),
   path('loginsubmit', views.loginsubmit, name="login_submit_page"),
   path('logout', views.logout, name="logout_page"),
   path('verify/<int:id>', views.verify, name="verify_page"),
   path('verify_drop/', views.verify_drop, name="verify_drop"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)