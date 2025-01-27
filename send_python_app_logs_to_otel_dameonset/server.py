import logging
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_task(task_id):
    logger.info(
        f"Processing task {task_id}",
        extra={
            "task_id": task_id,
            "processor": "main",
            "timestamp": time.time()
        }
    )
   
    # Simulate work
    time.sleep(1)
   
    logger.info(
        f"Completed task {task_id}",
        extra={
            "task_id": task_id,
            "status": "completed"
        }
    )

def main():
   logger.info("Application starting")
   i = 0
   while True:
       i += 1
       process_task(i)
   logger.info("Application shutdown")

if __name__ == "__main__":
   main()
