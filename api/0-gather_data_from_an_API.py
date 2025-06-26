#!/usr/bin/python3
"""
Script to return TODO list information for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    done_tasks = [task for task in todos if task.get("completed")]
    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(done_tasks)}/{len(todos)}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")