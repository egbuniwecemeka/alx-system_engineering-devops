# 0x1B. Web stack debugging #4

In this project i am debugging my web server Nginx as it fails when a certain amount (2000) of request is served to it.

I used a benchmarking app __ApacheBench__ to stimulate HTTP requests to my web server. I did that with the below command

* ab -c 100 -n 2000 localhost/

From my response i noticed that some requests failed and some passed. The task now is debugging to have 0 failed request

I got to learn about "ULIMIT". ulimit 