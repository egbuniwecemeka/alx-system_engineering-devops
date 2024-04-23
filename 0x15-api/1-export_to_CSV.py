#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Base url for JSONPlaceholder API
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user info from API and convert to JSON object
    user = requests.get(url + "users/{}".format(user_id).json)

    # Extract username
    username = user.get("username")

    # Extract todo associated with user_id and convert to JSON object
    todos = requests.get(url + "todos", param={"username": user_id}).json

    # Iterate over todos items using list comprehension
    # Print(user ID, username, completion status, and title)
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writes = csv.writes(csvfile, quoting=csv.QUOTE_ALL)
        [writes.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
