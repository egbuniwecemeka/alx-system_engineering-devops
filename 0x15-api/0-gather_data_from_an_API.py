#!/usr/bin/python3
"""
    Python script using REST API to return employee TODO list progress
    You must use urllib or requests module
    must accept an integer as a parameter, which is the employee ID    
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]

    #HTTP Req to API for user_id
    user_response = requests.get(url + "users/{}".format(user_id))

    # Convert response to dict
    user = user_response.json()

    #HTTP Req to API to retrieve todo_list using user_id
    user_attr = {"userId": user_id}
    todo_response = requests.get(url + "todos", user_attr)

    #Convert response to dict/JSON
    todos = todo_response.json()

    #List to store completed task
    complete = [t.get("title") for t in todos if t.get("complete") is True]

    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                         len(complete), len(todos)))
    
    [print("\t {}".format(complete)) for c in complete]
