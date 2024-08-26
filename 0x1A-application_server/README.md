# 0x1A. Application server

* All python scripts were written using python3
* All config files have comments

## Task 0 and 1

## Installation and configuration

    -   Log into webserver (SSH Login)
    -   Clone application repo to server
    -   update libraries (sudo apt-get update)
    -   create a virtual environment (venv)
    -   install dependencies in virtual environment (net-tools, gunicorn, flask)
    -   Install flask and gunicorn (pip install gunicorn flask)
    -   Test the route and ensure it is serving a response.
    -   WSGI Entry point for our application (wsgi.py)
    -   wsgi.py tells gunicorn server how to interact with our application.

## Task 2

    -   file: 2-app_server-nginx_config. The below processes where written into my configuration files to pass the assigned requirements.
    -   configure nginx to proxy request to the listening process on port 5000 (proxy_pass)
    -   configure nginx to serve pages from the route /airbnb-onepage/ (location block, proxy_pass, URL)
    -   configure nginx to serve the page locally and on its public IP on port 80 (listen => :80 and server_name IP addres )

## Task 3

    - location blocks are used to determine how to process the request URI (ie the part after the domain name or IP address)
    - location block optional modifiers include: none, = (exact match), ~ (case sensitive), ~* (case insensitive match), ^~ (prefix-based matching with high priority), 
    - The above specify how location block should be interpreted

Understanding how nginx chooses the location to handle the request is crucial to configure nginx accuurately. Nginx evaluates possible location contexts by comparing request URI to each location.

    - Firstly, nginx checks all prefix-based location matches (matches not containing regular expressions)
    - Nginx looks for exact match.
    - If no exact match type is found, nginx moves on to non-exact prefixes (discovering the longest matching prefix location for URI). It has the following conditions
        - If the longest matching prefix location has ^~, nginx ends it search.
        - If longest match prefix does not have ^~, the match is temporarily stored. 
    - After longest matching prefix have been determined, nginx moves on to determining reqular expressions location (case sensitive and case insensitive). If any, regular expression locations, within longest matching prefix, its moved to top of the list. Therefore, __first__ matching request URI regular expression location is selected to serve the request
    - If no regular expression location match the request URI, the previously stored prefix location is used

Note: positioning in configuration has a vast implication because while prefix matches selects request based on longest matching location, regular expression matches stop one the first match is found.

## When does Location Block Evaluation Jump to Other Locations?

Although a location serves a request based on its conents, there are certain directives that can cause for a location block to refer to another. These include index, try_files, rewrite, error_page

    - index: leads to an internal redirect if it is used to handle the request.
    - try_file: Tells Nginx to check for the existence of a file or directory. The last parameter can be the URI that nginx makes internal redirect too.
    - rewrite: if used together with the last parameter, or no parameter, nginx searches for a new matching location based on the results of the rewrite. eg (rewrite ^/rewriteme/(.*)$ /$1 last)
    - error_page: can create internal redirects similar to try_files, this directive is used to define what should happen when certain status codes are encountered. These are mostly not executed if try_files are set, as try_files handles the life cycle of requests.

## Understanding nginx location blocks and rewrite rules

    - use the break command to stop matching or parsing in blocks.
    - last tells nginx to restart its url matching process from the beginning but using newly written url
