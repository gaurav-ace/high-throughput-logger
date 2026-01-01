from naive_logger import  NaiveLogger
import time

def benchmark():
    logger = NaiveLogger("naive.log")

    NUM_LOGS = 10000

    start = time.time()

    for i in range(NUM_LOGS):
        logger.log("INFO", f"log message {i}")

    end = time.time()

    duration = end - start

    print("Naive Logger Benchmark")
    print("----------------------")
    print(f"Logs written : {NUM_LOGS}")
    print(f"Time taken  : {duration:.2f} seconds")
    print(f"Logs/sec   : {NUM_LOGS / duration:.0f}")


if __name__ == "__main__":
    benchmark()
