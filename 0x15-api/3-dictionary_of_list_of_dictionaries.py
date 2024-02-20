#!/usr/bin/python3
"""Module for using REST API from JSONPlaceholder."""


import json
import requests


def main():
    """The main entry point of the module."""
    users_url = f'https://jsonplaceholder.typicode.com/users'
    r_users = requests.get(users_url)
    users_list = r_users.json()
    todo_url = f'https://jsonplaceholder.typicode.com/todos'
    r_todo = requests.get(todo_url)
    todo_list = r_todo.json()
    users_data = dict()

    for user in users_list:
        user_todo_list = list()

        for todo in todo_list:
            if todo['userId'] == user['id']:
                user_todo_list.append({'username': user['username'],
                                       'task': todo['title'],
                                       'completed': todo['completed']})

        users_data[user['id']] = user_todo_list

    with open(f'todo_all_employees.json', mode='w', encoding='utf-8') as w_f:
        json.dump(users_data, w_f)


if __name__ == "__main__":
    main()
