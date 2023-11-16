#!/usr/bin/python3
'''Module api documentation'''
import requests
import sys


def get_employee_todo_progress(employee_id):
    '''Getting the employee todo progress'''

    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError('Employee id should be a positive integer')

    url_users = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response_users = requests.get(url_users)

    if response_users.status_code == 200:
        employee_data = response_users.json()
        employee_name = employee_data['name']

        url_todos = (f'https://jsonplaceholder.typicode.com/todos/'
                     f'?userId={employee_id}')
        response_todos = requests.get(url_todos)
        tasks_done = []

        if response_todos.status_code == 200:
            todos_data = response_todos.json()
            tasks_done = [todo for todo in todos_data if todo['completed']]
            num_done = len(tasks_done)
            num_total = len(todos_data)

            message = (f'Employee {employee_name} is done with tasks'
                       f'({num_done}/{num_total}):')
            print(message)

            for task in tasks_done:
                title = task['title']
                print(f'\t {title}')
        else:
            print(f'Error: Failed to retrieve information for employee'
                  f' {employee_id}. Status code: {response_todos.status_code}')
    else:
        print(f'Error: Failed to retrieve information for employee ID'
              f' {employee_id}. Status code: {response_users.status_code}')


if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
        exit(1)
