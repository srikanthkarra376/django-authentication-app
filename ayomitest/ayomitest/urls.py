
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profiles/$', views.profiles_view, name='profiles'),
    url(r'^profiles/(?P<id>\d+)/edit/$', views.edit_view, name='edit'),
    url(r'^$', views.home_view, name='home'),

]

