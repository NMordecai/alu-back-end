 #!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # --- 1. Fetch Employee Name ---
    user_url = f"{base_url}/users/{employee_id}"
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        employee_data = user_response.json()
        employee_name = employee_data.get("name")

        if not employee_name:
            print(f"Error: Employee with ID {employee_id} not found or name missing.")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee data for ID {employee_id}: {e}")
        return
    except ValueError:
        print(f"Error: Could not decode JSON from user data for ID {employee_id}.")
        return

    # --- 2. Fetch Employee's TODO List ---
    todos_url = f"{base_url}/todos?userId={employee_id}"
    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        tasks_data = todos_response.json()

        if not tasks_data:
            print(f"Employee {employee_name} has no tasks found.")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error fetching tasks for employee ID {employee_id}: {e}")
        return
    except ValueError:
        print(f"Error: Could not decode JSON from tasks data for ID {employee_id}.")
        return

    # --- 3. Process Tasks ---
    total_tasks = len(tasks_data)
    completed_tasks = []
    for task in tasks_data:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))

    number_of_done_tasks = len(completed_tasks)

    # --- 4. Display Results ---
    # First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    # Second and N next lines display the title of completed tasks: (tab and space before title)
    for title in completed_tasks:
        print(f"\t {title}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <employee_id>")
        print("Example: python your_script_name.py 1")
        sys.exit(1)

    try:
        employee_id_input = int(sys.argv[1])
        if employee_id_input <= 0:
            print("Error: Employee ID must be a positive integer.")
            sys.exit(1)
        get_employee_todo_progress(employee_id_input)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

