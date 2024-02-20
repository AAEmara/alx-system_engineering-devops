#!/usr/bin/python3
"""Module for using REST API from JSONPlaceholder."""


import json
import requests
import sys


def main():
    """The main entry point of the module."""
    user_id = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    r_user = requests.get(user_url)
    user_dict = r_user.json()
    todo_url = f'https://jsonplaceholder.typicode.com/todos'
    r_todo = requests.get(todo_url)
    todo_list = r_todo.json()
    todo_count = 0
    todo_done = 0
    done_list = list()
    user_todo_list = list()

    for todo in todo_list:
        if todo['userId'] == user_id:
            todo_count += 1
            user_todo_list.append(todo)
        if todo['completed'] is True and todo['userId'] == user_id:
            todo_done += 1
            done_list.append(todo)

    name = user_dict['name']
    print(f"Employee {name} is done with tasks({todo_done}/{todo_count}):")
    for todo in done_list:
        print(f"\t {todo['title']}")

    obj_dict = dict()
    value_list = list()
    for task in user_todo_list:
        value_list.append({'task': task['title'],
                           'completed': task['completed'],
                           'username': user_dict['username']})
    obj_dict[user_id] = value_list
    with open(f'{user_id}.json', mode='w', encoding='utf-8') as w_file:
        json.dump(obj_dict, w_file)


if __name__ == "__main__":
    main()
