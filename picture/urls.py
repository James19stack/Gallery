from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^people/$',views.people,name = 'people'),
    url(r'^travel/$',views.travel,name = 'travel'),
    url(r'^food/$',views.food,name = 'food'),
    url(r'^search/$',views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

