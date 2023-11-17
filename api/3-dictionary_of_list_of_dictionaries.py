#!/usr/bin/python3
'''Module api documentation'''
import json
import requests


def get_employee_todo_progress():
    '''Getting the employee todo progress'''

    all_employees_data = {}
    for employee_id in range(1, 11):
        url_users = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        response_users = requests.get(url_users)

        if response_users.status_code == 200:
            employee_data = response_users.json()
            username = employee_data['username']

            url_todos = (f'https://jsonplaceholder.typicode.com/todos/'
                         f'?userId={employee_id}')
            response_todos = requests.get(url_todos)

            if response_todos.status_code == 200:
                todos_data = response_todos.json()

                for task in todos_data:
                    all_employees_data.setdefault(employee_id, []).append({
                        'username': username,
                        'task': task['title'],
                        'completed': task['completed']
                    })

                with open('todo_all_employees.json', 'w') as jf:
                    json.dump(all_employees_data, jf)
            else:
                print(f'Error: Failed to retrieve information for employee'
                      f' {employee_id}. Status code:
                      {response_todos.status_code}')
        else:
            print(f'Error: Failed to retrieve information for employee ID'
                  f' {employee_id}. Status code: {response_users.status_code}')


if __name__ == '__main__':
    try:
        get_employee_todo_progress()
    except ValueError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
        exit(1)
