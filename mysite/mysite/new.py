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
    callbacks=playbook_cb,
    runner_callbacks=runner_cb,
    stats=stats,
    # private_key_file='/path/to/key.pem'
)

results = pb.run()

# Ensure on_stats callback is called
# for callback modules
playbook_cb.on_stats(pb.stats)

os.remove(hosts.name)

print results


from ansible.playbook import PlayBook
pb = PlayBook(playbook='/home/ec2-user/hack/speeds/mysite/py.yaml')
pb.run()