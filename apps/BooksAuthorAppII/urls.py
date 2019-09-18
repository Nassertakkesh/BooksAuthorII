from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^book$', views.homepage),
    url(r'^addingbook$', views.addingbook),
    url(r'^authors$', views.authors),
    url(r'^book/(?P<id>\d+)$', views.books_page),
    url(r'^authors/(?P<id>\d+)$', views.authors_page),
    url(r'^authors/addingbooktoauthor$', views.addingbooktoauthor),
    url(r'^addingauthor$', views.addingauthor),

]