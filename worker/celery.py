from celery import Celery
import os

# 从环境变量获取Redis主机，默认为localhost
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_url = f"redis://{redis_host}:6379/0"

app = Celery("celery", broker=redis_url, backend=redis_url)

# 配置队列
app.conf.task_queues = {
    'fast_queue': {
        'exchange': 'fast_exchange',
        'routing_key': 'fast',
    },
    'slow_queue': {
        'exchange': 'slow_exchange',
        'routing_key': 'slow',
    },
    'default': {
        'exchange': 'default_exchange',
        'routing_key': 'default',
    },
}

# 配置路由
app.conf.task_routes = {
    'worker.tasks.processing_tasks.fast_*': {'queue': 'fast_queue'},
    'worker.tasks.processing_tasks.slow_*': {'queue': 'slow_queue'},
    'worker.tasks.math_tasks.*': {'queue': 'default'},
}

# 自动发现任务
app.autodiscover_tasks(['worker.tasks']) 