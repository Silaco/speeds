from django.conf.urls import url

# from mysite.views import MyView
# from mysite.views import CurrentClass
# from mysite.views import Simple
from mysite.views import LoggedIn
# from mysite.views import AnsibleInvoke1
from mysite.views import Login,get,login,index,check

urlpatterns = [
    # url(r'^hello/$', MyView.as_view(), name='my-view'),
	# url(r'^current/$', CurrentClass.as_view(), name='my-current'),
	url(r'^Login/$', Login, name='my-view'),
	# url(r'^invoke/$', AnsibleInvoke.Invoke),
    # url(r'^search/$', Simple.search),
	url(r'^run/$', get, name='new-view11'),
	url(r'^index/$', index, name='new-view11q'),
	url(r'^login/$', login, name='login-view11'),
	url(r'^check/$', check, name='check'),
	url(r'^', index, name='home'),
]

