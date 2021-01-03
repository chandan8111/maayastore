# maayastore
Django Website ( ecommerse and blog application )



# Deploy application on ubunte

Requirement | Commend
------------ | -------------
update os | <pre><code>sudo apt update</code></pre
upgade | <pre><code>sudo apt install upgrade</code></pre
install apache | <pre><code>sudo apt install apache2</code></pre
apache firewall info | <pre><code>ufw app info "Apache Full"</code></pre
allow permittions to firewall | <pre><code>ufw allow in "Apache Full"</code></pre
install python 3 pip | <pre><code>apt install python3-pip</code></pre
apache mod wsgi | <pre><code>apt install libapache2-mod-wsgi-py3</code></pre
change dir | <pre><code>cd /var/www</code></pre
make dir | <pre><code>mkdir dir_name</code></pre
change dir | <pre><code>cd dir_name</code></pre
install virtual environment | <pre><code>pip3 install virtualenv</code></pre
create virtual environment | <pre><code>virtualenv env_name</code></pre
activate virtual environment | <pre><code>source env_name/bin/activate</code></pre
install django | <pre><code>pip3 install django</code></pre
make project in django | <pre><code>django-admin startproject project_name .</code></pre
change dir | <pre><code>cd project_name</code></pre
open settings.py file | <pre><code>vim settings.py</code></pre
change in settings.py | <pre> and host_ip into allowed_host [] and below of static url <code>STATIC_ROOT = os.path.join(BASE_DIR, "static/")</code>press Esc > : > wq</pre
change dir | <pre><code>cd ..</code></pre
make migrations | <pre><code>python manage.py makemigrations</code></pre
migrate | <pre><code>python manage.py migrate</code></pre
create superuser | <pre><code>python manage.py createsuperuser</code></pre
collect static | <pre><code>python manage.py collectstatic</code></pre
run django server | <pre><code>python manage.py runserver 0.0.0.0:8000</code></pre
change dir | <pre><code>cd /etc/apache2/sites-availiable/</code></pre










_You **can** combine them_

http://github.com - automatic!
[GitHub](http://github.com)
