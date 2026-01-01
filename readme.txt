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


