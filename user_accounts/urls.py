from django.conf.urls import patterns, url

from .views import LoginView
from .views import LoginView2
from .views import LogoutView

urlpatterns = patterns('',
    url(r'^login2/', LoginView.as_view(), name='login2'),
    url(r'^login/', LoginView2.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    #url(r'^login/', include('user_accounts.urls')),
)