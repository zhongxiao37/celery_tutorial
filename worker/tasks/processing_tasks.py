from worker.celery import app
import time

# 快速处理任务
@app.task(name="worker.tasks.processing_tasks.fast_process")
def fast_process(x, y):
    """一个快速处理的任务"""
    return x + y

@app.task(name="worker.tasks.processing_tasks.fast_operation")
def fast_operation(data):
    """另一个快速处理的任务"""
    return data * 2

# 慢速处理任务 
@app.task(name="worker.tasks.processing_tasks.slow_process")
def slow_process(x, y):
    """一个需要较长时间处理的任务"""
    time.sleep(10)  # 模拟耗时操作
    return x + y

@app.task(name="worker.tasks.processing_tasks.slow_operation")
def slow_operation(data):
    """另一个耗时任务"""
    time.sleep(5)  # 模拟耗时操作
    return data * 3 