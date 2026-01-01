import threading
import time
from queue import Queue

class AsyncLogger:
    """
    Asynchronous logger using producer-consumer model.
    Application threads enqueue log messages.
    A single background thread writes them to disk.
    """

    def __init__(self, filename, queue_size=10000):
        # Path of log file
        self.filename = filename

        # Thread-safe queue for log messages
        self.queue = Queue(maxsize=queue_size)

        # Event used to signal logger thread to stop
        self.stop_event = threading.Event()

        # Background thread responsible for disk I/O
        self.worker = threading.Thread(
            target=self._logger_thread,
            daemon=True
        )

        # Start background logger thread
        self.worker.start()

    def log(self, level, message):
        """
        Called by application threads.
        This function should be FAST and NON-BLOCKING.
        """

        timestamp = time.time()
        log_line = f"{timestamp} [{level}] {message}\n"

        try:
            # Put log message into queue
            # If queue is full, this will block briefly
            self.queue.put(log_line, block=True)
        except Exception:
            # In real systems, you may drop logs here
            pass

    def _logger_thread(self):
        """
        Background thread.
        Continuously reads from queue and writes to disk.
        """

        # Open file ONCE (important optimization)
        with open(self.filename, "a") as f:
            while not self.stop_event.is_set():
                try:
                    # Wait for log message
                    log_line = self.queue.get(timeout=0.5)

                    # Write to file (disk I/O happens here)
                    f.write(log_line)

                    # Mark task as done
                    self.queue.task_done()

                except Exception:
                    # Timeout or empty queue → loop again
                    continue

            # Drain remaining messages before exit
            while not self.queue.empty():
                f.write(self.queue.get())
                self.queue.task_done()

            # Ensure everything is flushed to disk
            f.flush()

    def shutdown(self):
        """
        Gracefully stop logger thread.
        """
        self.stop_event.set()
        self.worker.join()

