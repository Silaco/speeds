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
		from ansible.playbook import PlayBook
		from ansible.inventory import Inventory
		from ansible import callbacks
		from ansible import utils

		import jinja2
		from tempfile import NamedTemporaryFile
		import os

		# Boilerplace callbacks for stdout/stderr and log output
		utils.VERBOSITY = 0
		playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
		stats = callbacks.AggregateStats()
		runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

		# Dynamic Inventory
		# We fake a inventory file and let Ansible load if it's a real file.
		# Just don't tell Ansible that, so we don't hurt its feelings.
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

		pb = PlayBook(
			playbook='/home/ec2-user/hack/speeds/mysite/py.yaml',
			host_list=hosts.name,     # Our hosts, the rendered inventory file    
			# callbacks=playbook_cb,
			# runner_callbacks=runner_cb,
			stats=stats,
			# private_key_file='/path/to/key.pem'
		)

		results = pb.run()

		# Ensure on_stats callback is called
		# for callback modules
		playbook_cb.on_stats(pb.stats)

		os.remove(hosts.name)

		print results
		
		return HttpResponse('<table>%s</table>' % '\n'.join(html))


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