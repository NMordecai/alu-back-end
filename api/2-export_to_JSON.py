#!/usr/bin/python3
"""
Exports tasks for a given employee ID to JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
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
    username = user_response.json().get("username")
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    tasks = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    } for task in todos]

    output_data = {str(employee_id): tasks}
    filename = f"{employee_id}.json"
    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(output_data, jsonfile)