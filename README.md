# RabbitMQ messaging

This getting started follows
https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/

## Install

```
pip install -r requirements.txt

# plus the docker env and container
```

## Run Testapp

```
# run worker
celery -A rabbitmq worker --loglevel info

# run task
python -m rabbitmq.run_tasks
```

## Run docker container

```
docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -e RABBITMQ_DEFAULT_VHOST=vhost -p 8080:15672 -p 5672:5672 rabbitmq:3-management
```
