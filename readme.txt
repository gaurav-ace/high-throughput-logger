 high throughput
 non-blocking API
 configurable queue size
 performance benchmark


starting with Naive solution : 
-> there will be an application thread -> open-> write(log)-> close  -> file/disk

this is having many issues like blocking i/o, low throughput etc.. 

but good to start with.

Application thread
      |
      v
 open → write → close   (every log)
      |
      v
   Disk I/O (blocking)


output of benchmark (writing 10000 logs) : 
Naive Logger Benchmark
----------------------
Logs written : 10000
Time taken  : 0.27 seconds
Logs/sec   : 36985


phase 2 : async model : 

Application threads
        |
        v
  log() puts message
        |
        v
   ┌────────────┐
   │   Queue    │   (thread-safe)
   └────────────┘
        |
        v
  Logger thread
        |
        v
      File I/O


no blocking I/O
log() is taking very little time as it is not accessing the disk. It writes to in-memory queue.

one worker thread handles the  write part separately.

Async Logger Benchmark
----------------------
Logs written : 10000
Time taken  : 0.04 seconds     >>> almost 8 times faster
Logs/sec   : 262850


