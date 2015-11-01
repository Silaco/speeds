from django.conf.urls import url

# from mysite.views import MyView
# from mysite.views import CurrentClass
# from mysite.views import Simple
# from mysite.views import LoggedIn
# from mysite.views import AnsibleInvoke1
from mysite.views import Login,get,login,index,check,saveHost,Hosts,audit,home

urlpatterns = [
	url(r'^Login/$', Login, name='my-view'),
	url(r'^run/$', get, name='new-view11'),
	url(r'^index/$', home, name='new-view11q'),
	url(r'^login/$', login, name='login-view11'),
	url(r'^RDM/$', check, name='check'),
	# url(r'home^', Login, name='home'),
	url(r'^hosts/$', Hosts, name='SaveHost'),
	url(r'^home/$', home, name='SaveHost'),
	url(r'^submithost/$', saveHost, name='SaveHost'),
	url(r'^Execute/$', get, name='Execute'),
	url(r'^audit/$', audit, name='audit'),
	
]

