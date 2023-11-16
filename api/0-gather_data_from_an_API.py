#!/usr/bin/python3
'''Module api documentation'''
import requests
import sys


def get_employee_todo_progress(employee_id):
    '''Getting the employee todo progress'''

    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError('Employee id should be a positive integer')

    url = f'https://jsonplaceholder.typicode.com/user/{employee_id}'
    api_url_response = requests.get(url)

    if api_url_response.status_code == 200:
        data = api_url_response.json()

        tasks_done = [todo for todo in data['todos'] if todo['completed']]
        num_done = len(tasks_done)
        num_total = len(data['todos'])
        employee_name = data['name']

        message = f'Employee {employee_name} is done with tasks\
            ({num_done}/{num_total})'
        print(message)

        for task in tasks_done:
            title = task['title']
            print(f'\t {title}')
    else:
        print(f'Error: Failed to retrieve information.\
              Status code: {api_url_response.status_code}')


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
