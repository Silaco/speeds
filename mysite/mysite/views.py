from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import View
from django.shortcuts import render
import sqlite3

class MyView(View):
	def get(self, request, *args, **kwargs):		
		conn = sqlite3.connect('test.db')
		cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
		html = []
		for row in cursor:
			html.append('<tr><td>'+str(row[0])+'</td><td>'+row[1]+'</td><td>'+row[2]+'</td><td>'+str(row[3])+'</td></tr>')
		conn.close()			
		return HttpResponse('<table>%s</table>' % '\n'.join(html))

class AnsibleInvoke1(View):
	def get(self, request, *args, **kwargs):		
		import os
		data=os.system("ansible-playbook /home/ec2-user/hack/speeds/mysite/py.yaml -i hosts")
		
		return HttpResponse(data)


class CurrentClass(View):
	def get(self, request, *args, **kwargs):	
		import os.path
		Temp_Path = os.path.realpath('.')
		template=loader.get_template('ShowTime.htm')
		context=Context({'Test':1})
		return HttpResponse(template.render(context))

class Simple(View):		
	def search_form(request):
		return render(request, 'search_form.htm')
	def search(request):
		if 'id' in request.GET:
			name=request.GET['name']
			id=request.GET['id']
			address=request.GET['address']
			salary=request.GET['salary']	
			
			# conn = sqlite3.connect('test.db')
			
			# conn.execute();
			
			sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES ("+id+", '"+name+"', 32, '"+address+"', "+salary+" )"
			
			conn = sqlite3.connect('test.db')
			
			conn.execute(sql);
			conn.commit();
			message = sql
		else:
			message = 'You submitted an empty form.'
		return HttpResponse(message)
		
class AnsibleInvoke(View):		
	def Invoke(request):
		
		import ansible.runner

		runner = ansible.runner.Runner(
		   module_name='ping',
		   module_args='',
		   pattern='web*',
		   forks=10
		)
		datastructure = runner.run()
		
		html = []
		for row in cursor:
			html.append('<tr><td>'+str(row[0])+'</td><td>'+row[1]+'</td><td>'+row[2]+'</td><td>'+str(row[3])+'</td></tr>')
		# conn.close()			
		return HttpResponse('<table>%s</table>' % '\n'.join(html))

		return render(request, 'search_form.htm')