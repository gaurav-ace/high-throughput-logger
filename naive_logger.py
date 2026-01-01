import time

class NaiveLogger:


    def __init__(self, filename):
        # filename is stored
        self.filename = filename

    def log(self, level, message):
        """
        Writes a single log message to disk.
        This function BLOCKS until disk I/O completes.
        """

        timestamp = time.time()

        # call transfers to OS, it opens a file
        with open(self.filename, "a") as f:  # open file in append mode

            log_line = f"{timestamp} [{level}] message\n"
            
            # write to disk(syscall)
            f.write(log_line)

        # closing a file automatically flushes.

        #blocking the thread till whole ops is finished





