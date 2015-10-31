from django.conf.urls import url

# from mysite.views import MyView
# from mysite.views import CurrentClass
# from mysite.views import Simple
from mysite.views import LoggedIn
from mysite.views import AnsibleInvoke1


urlpatterns = [
    # url(r'^hello/$', MyView.as_view(), name='my-view'),
	# url(r'^current/$', CurrentClass.as_view(), name='my-current'),
	url(r'^LoggedIn/Login$', LoggedIn.Login, name='LoggedIn'),
	# url(r'^invoke/$', AnsibleInvoke.Invoke),
    # url(r'^search/$', Simple.search),
	url(r'^run/$', AnsibleInvoke1.as_view(), name='new-view11'),
]

