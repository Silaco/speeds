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
	try:
		key = request.session['access_key']
		age = request.session.get_expiry_age()
		if age > 10:
			index(request)
	except:
		return HttpResponse('error')
	template=loader.get_template('Run.htm')
	a=range(1,100)
	import os
	name=os.getcwd() 
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT DISTINCT GROUPNAME from HOSTS")
	html = []
	for row in cursor:
		html.append(str(row[0]))
	conn.close()			
	context=Context({'Test':os.listdir(name+"/mysite/playbooks/"),'value':html})
	# return HttpResponse(template.render(context))
	return render(request, 'Run.htm',context)	
def login(request):
	message = 'You submitted an empty form.'
	
	if 'user' in request.POST:
		name=request.POST['user']
		pwd=request.POST['pwd']
		
		if name=='testuser' and pwd=='testpwd':
			request.session['access_key'] = name
			request.session.set_expiry(60)
			# return render(request, 'Hosts.htm')
			return HttpResponse('Welcome :'+name)
			# get(request)
		message = 'Invalid.'
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

def Hosts(request):	
	# template=loader.get_template('Hosts.htm')	
	return render(request, 'Hosts.htm')
def saveHost(request):
	message = 'You submitted an empty form.'
	# if request.session.test_cookie_worked():
		# return render(request, 'Hosts.htm')
	# request.session.set_test_cookie()
	
	if 'Name' in request.POST:
		Name=request.POST['Name']
		Group=request.POST['Group']
		
		sql = "INSERT INTO HOSTS (NAME,GROUPNAME) VALUES ('"+Name+"','"+Group+"' )"
			
		conn = sqlite3.connect('test.db')

		conn.execute(sql);
		conn.commit();
		message = 'Name : '+Name
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
	
def get(request):
	try:
		key = request.session['access_key']
		age = request.session.get_expiry_age()
		if age > 10:
			index(request)
	except:
		return HttpResponse('error')
		
	import jinja2
	from tempfile import NamedTemporaryFile
	import os
	inventory = """
	[current]
	{{ public_ip_address }}
	"""
	inventory_template = jinja2.Template(inventory)
	rendered_inventory = inventory_template.render({
		'public_ip_address': 'localhost'    
		# and the rest of our variables
	})

	# Create a temporary file and write the template string to it
	hosts = NamedTemporaryFile(delete=False)
	hosts.write(rendered_inventory)
	hosts.close()
	import commands
	name=os.getcwd() 
	name=name+"/mysite/playbooks/"
	playBook=request.GET['playBook']
	Group=request.GET['Group']
	name=name+playBook
	ret = commands.getoutput("ansible-playbook "+name+" -i "+hosts.name)
	# print ret
	log=ret
	from datetime import datetime
	
	sql = "INSERT INTO AUDIT (USER,LOG,TRANSDATE) VALUES ('"+request.session['access_key']+"','"+log+"','"+str(datetime.now())+"' )"
		
	conn = sqlite3.connect('test.db')

	conn.execute(sql);
	conn.commit();
	template=loader.get_template('Results.htm')
	context=Context({'Test':ret.replace('\n','<BR/>')})
	return HttpResponse(template.render(context))
	
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