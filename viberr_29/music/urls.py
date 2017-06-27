from django.conf.urls import url
from . import views         # from current directory import views
from django.contrib.auth import views as auth_views

app_name = 'music'  #we use this so that when we use the name='detail' in our html it would know that the detail under here is wat it will use

urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),    #views.IndexView.as_view() - since it was suppose to be a function
                                                            #we just call the class views.Index View then convert/treat it as a function using .as_view()

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^log-in/$', views.LoginFormView.as_view(), name='log-in'),

    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    # url(r'^login/$', auth_views.login, {'template_name': 'music/login.html'}, name='login'),
    #
    # url(r'^logout/$', auth_views.logout, {'template_name': 'music/logout.html'}, name='logout'),

    #/music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), # everytime we are using DetailView it would always expect the PK
                                                                            # there for (?P<pk>[0-9]+)/$
    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),  # we don't need to specify the pk since we still dont have it yet. we are still creating the objecf

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),








]