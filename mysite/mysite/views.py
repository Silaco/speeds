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

def Login(request):	
	# template=loader.get_template('Login.htm')	
	return render(request, 'Login.htm')

def index(request):	
	if request.session.test_cookie_worked():
		return render(request, 'Hosts.htm')
	return render(request, 'Login.htm')
	
def check(request):	
	key = request.session['access_key']
	age = request.session.get_expiry_age()
	if age > 10:
		index(request)
	template=loader.get_template('Run.htm')
	a=range(1,100)
	import os
	name=os.getcwd() 
	context=Context({'Test':os.listdir(name+"/mysite/playbooks/"),'value':name})
	return HttpResponse(template.render(context))
	
def login(request):
	message = 'You submitted an empty form.'
	# if request.session.test_cookie_worked():
		# return render(request, 'Hosts.htm')
	# request.session.set_test_cookie()
	
	if 'user' in request.POST:
		name=request.POST['user']
		pwd=request.POST['pwd']
		
		if name=='testuser' and pwd=='testpwd':
			request.session['access_key'] = name
			request.session.set_expiry(4)
			return render(request, 'Hosts.htm')
			# get(request)
		message = 'Invalid.'
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
	
def get(request):
		if request.session.test_cookie_worked():			
			import jinja2
			from tempfile import NamedTemporaryFile
			import os
			inventory = """
			[current]
			{{ public_ip_address }}
			"""
			inventory_template = jinja2.Template(inventory)
			rendered_inventory = inventory_template.render({
				'public_ip_address': '111.222.333.444'    
				# and the rest of our variables
			})

			# Create a temporary file and write the template string to it
			hosts = NamedTemporaryFile(delete=False)
			hosts.write(rendered_inventory)
			hosts.close()
			import commands
			ret = commands.getoutput("ansible-playbook /home/ec2-user/hack/speeds/mysite/py.yaml -i "+hosts.name)
			# print ret

			template=loader.get_template('Results.htm')
			context=Context({'Test':ret.replace('\n','<BR/>')})
			return HttpResponse(template.render(context))
		else:
			return render(request, 'Login.htm')
			

class CurrentClass(View):
	def get(self, request, *args, **kwargs):	
		import os.path
		Temp_Path = os.path.realpath('.')
		template=loader.get_template('ShowTime.htm')
		context=Context({'Test':1})
		return HttpResponse(template.render(context))

class LoggedIn(View):		
	def Login(request):
		return render(request, 'Login.htm')
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