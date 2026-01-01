from async_logger import AsyncLogger
import time

def benchmark():
    logger = AsyncLogger("async.log")

    NUM_LOGS = 10000

    start = time.time()

    for i in range(NUM_LOGS):
        logger.log("INFO", f"log message {i}")

    end = time.time()

    # Shutdown logger gracefully
    logger.shutdown()
    
    duration = end - start

    print("Async Logger Benchmark")
    print("----------------------")
    print(f"Logs written : {NUM_LOGS}")
    print(f"Time taken  : {duration:.2f} seconds")
    print(f"Logs/sec   : {NUM_LOGS / duration:.0f}")


if __name__ == "__main__":
    benchmark()
