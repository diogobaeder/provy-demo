from commands import getoutput

from fabric.api import cd, env, run

from provyfile import VM_IP


env.hosts = [VM_IP]
env.user = 'vagrant'
env.password = 'vagrant'


SITE_PATH = '/home/vagrant/provy-demo/demo/'
BROWSER = 'google-chrome'


def start():
    with cd(SITE_PATH):
        run('gunicorn --daemon demo.wsgi:application', pty=False)


def show():
    url = 'http://%s:8000' % VM_IP
    print getoutput('%s %s' % (BROWSER, url))