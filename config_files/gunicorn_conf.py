# user = 'www-data'
# group = 'www-data'
bind = '0.0.0.0:5000'
#workers = ${WORKERS}
access_log_format = '"%({x-real-ip}i)s" %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = '/var/log/mitoage/mitoage.access.log'
errorlog = '/var/log/mitoage/mitoage.error.log'
loglevel = 'warn'
timeout = 120
graceful_timeout = 90
#worker_class = 'gevent'
#chdir = '/srv/mitoage/mitoage'
chdir = '/srv/www'
