from fabric.api import cd, env, run, local

from provyfile import VM_IP


env.hosts = [VM_IP]
env.user = 'vagrant'
env.password = 'vagrant'


SITE_PATH = '/home/vagrant/provy-demo/demo/'
BROWSER = 'google-chrome'


def start():
    with cd(SITE_PATH):
        run('gunicorn --daemon -b 0.0.0.0:8000 demo.wsgi:application', pty=False)


def show():
    url = 'http://localhost:8001'
    local('%s %s' % (BROWSER, url))