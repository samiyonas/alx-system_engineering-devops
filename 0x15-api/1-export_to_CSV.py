#!/usr/bin/python3
""" gather data from an API """
import requests
from sys import argv


if __name__ == "__main__":
    res_1 = requests.get("https://jsonplaceholder.typicode.com/users")
    res_2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    res_1 = res_1.json()
    res_2 = res_2.json()

    Id = int(argv[1])
    name = res_1[Id - 1].get("username")
    tasks = 0
    to_csv = []

    for i in range((Id - 1) * 20, ((Id - 1) * 20) + 20):
        is_completed = res_2[i].get("completed")
        title = res_2[i].get("title")

        line = f'"{Id}","{name}","{is_completed}","{title}"\n'
        to_csv.append(line)

    with open("{}.csv".format(Id), 'w') as f:
        for i in to_csv:
            f.write(i)
