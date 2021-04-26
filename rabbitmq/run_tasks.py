from rabbitmq.tasks import longtime_add
import time


if __name__ == "__main__":
    result = longtime_add.delay(1, 2)
    # at this time, our task is not finished, so it will return False
    print(f"Task finished? {result.ready()}")
    print(f"Task result: {result.result}")
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print(f"Task finished? {result.ready()}")
    print(f"Task result: {result.result}")
