from django.urls import  re_path
from bbc import views

urlpatterns = [
	re_path(r'^$', 				                    views.home, 		name = 'home'),
    re_path(r'^scrape/$', 		                    views.scrape, 		name = 'scrape'),
    re_path(r'^article/(?P<id>[0-9]+)$',   views.article,      name = 'article')
]