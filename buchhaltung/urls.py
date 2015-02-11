from django.conf.urls import patterns, include, url
from django.contrib import admin

#from bilanz.views import DashboardView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buchhaltung2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^bilanz/', include('bilanz.urls')),
    url(r'^', include('bilanz.urls')),
    #url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('user_accounts.urls')),
)
