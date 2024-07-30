#!/usr/bin/python3

""" A python script that uses REST API to get information from a server """

import requests
from sys import argv

if __name__ == "__main__":
    """ Program retrieves data from an API"""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./python_script employee_id")
        exit(1)

    emp_id = int(argv[1])
    url_todo = f'https://jsonplaceholder.typicode.com/todos'
    url_users = f'https://jsonplaceholder.typicode.com/users'

    # Fetch data
    response_todo = requests.get(url_todo)
    response_users = requests.get(url_users)
    data_todo = response_todo.json()
    data_users = response_users.json()

    # Filter todo and users response for specific employee id
    emp_tasks = [task for task in data_todo if task['userId'] == emp_id]
    users_name = [user for user in data_users if user['id'] == emp_id]

    # Calculate tasks
    total_tasks = len(emp_tasks)
    completed_tasks = sum([1 for task in emp_tasks if task['completed']])
    employee_name = users_name[0]['name'] if users_name else f"{emp_id}"
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Print title of completed tasks
    completed_tasks_title = [
            task['title']
            for task in emp_tasks
            if task['completed']
    ]
    print("\t" + "\n\t".join(completed_tasks_title))
