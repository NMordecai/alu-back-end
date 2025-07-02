#!/usr/bin/python3
"""
Exports all employees' TODO tasks to a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    users = users_response.json()
    todos = todos_response.json()
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = []

        for task in todos:
            if task.get("userId") == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_tasks[str(user_id)] = user_tasks
    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)
