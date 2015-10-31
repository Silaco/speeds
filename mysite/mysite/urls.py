from django.conf.urls import url

from mysite.views import MyView
from mysite.views import CurrentClass
from mysite.views import Simple



urlpatterns = [
    url(r'^hello/$', MyView.as_view(), name='my-view'),
	url(r'^current/$', CurrentClass.as_view(), name='my-current'),
	url(r'^search-form/$', Simple.search_form),	
    url(r'^search/$', Simple.search),
]

