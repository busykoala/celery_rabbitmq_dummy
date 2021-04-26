from celery import Celery


broker_url = 'amqp://user:password@localhost:5672/vhost'
app = Celery(
    "rabbitmq",  # py-pkg name
    broker=broker_url,
    backend="rpc://",
    include=["rabbitmq.tasks"],
)
