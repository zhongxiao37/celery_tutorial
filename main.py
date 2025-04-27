from worker.tasks.math_tasks import add, mul
from worker.tasks.processing_tasks import slow_operation

def main():
    print("Hello from celery-tutorial!")
    result = add.delay(4, 4)
    print(result.get())
    result = mul.delay(4, 4)
    print(result.get())
    result = slow_operation.delay(3)
    print(result.get())


if __name__ == "__main__":
    main()
