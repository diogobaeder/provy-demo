from fabric.api import cd, env, run


env.hosts = ['192.168.1.11']
env.user = 'vagrant'
env.password = 'vagrant'
SITE_PATH = '/home/vagrant/provy-demo/demo/'

def start():
    with cd(SITE_PATH):
        run('gunicorn --daemon demo.wsgi:application', pty=False)