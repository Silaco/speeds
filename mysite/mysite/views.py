from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import View

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
class CurrentClass(View):
	def get(self, request, *args, **kwargs):	
		import os.path
		Temp_Path = os.path.realpath('.')
		template=loader.get_template('ShowTime.htm')
		context=Context({'Test':1})
		return HttpResponse(template.render(context))