#!/usr/bin/python3

""" A python script that uses REST API to get information from a server """

import requests
from sys import argv
import csv

if __name__ == "__main__":
    """ Program retrieves data from an API"""
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./python_script employee_id")
        exit(1)

    emp_id = int(argv[1])

    # Get /todos response from an API
    url = f'https://jsonplaceholder.typicode.com/todos'
    response_todo = requests.get(url)
    data_todo = response.json()

    # Get /todos response from an API
    url = f'https://jsonplaceholder.typicode.com/users'
    response_user = requests.get(url)
    data_user = response.json()


    # Filter response for specific employee id
    emp_tasks = [task for task in data_todo if task['userId'] == emp_id]

    # Filter response for spicific username
    user_name = [user['name'] for task in emp_tasks if task['completed']])

    # Setting up csv file and format
    csv_file_name = f'{emp_id}'
    csv_data = []
    for data in emp_tasks:
        csv_data.append([
                str(emp_id), 
                employee_name,
                str(task['complete'],
                task['title'])
        ])

    with (csv_file_name, w, newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
