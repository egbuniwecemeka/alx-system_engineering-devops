# 0x1A. Application server

* All python scripts were written using python3
* All config files have comments

## Installation and configuration

    -   Log into webserver (SSH Login)
    -   Clone application repo to server
    -   update libraries (sudo apt-get update)
    -   Install flask and gunicorn (pip install gunicorn flask)
    -   Test the route and ensure it is serving a response.
    -   WSGI Entry point for our application (wsgi.py)
    - wsgi.py tells gunicorn server how to interact with our application.
    - 
