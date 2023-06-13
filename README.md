# E-summit Backend

## Usage
run ```pip install -r requirements.txt ``` before using the project

### Intilize reddis 

https://redis.io/docs/getting-started/installation/install-redis-on-windows/

### Create superuser

run ```python manage.py createsuperuser```

### run server

run ``` python manage.py runserver ```

### start Celery
run ```  celery -A esummit worker -l info -P gevent```
