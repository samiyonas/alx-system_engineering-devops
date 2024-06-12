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
    name = res_1[Id - 1].get("name")
    tasks = 0
    titles = []

    for i in range((Id - 1) * 20, ((Id - 1) * 20) + 20):
        if res_2[i].get("completed") is True:
            tasks += 1
            titles.append(res_2[i].get("title"))

    print("Employee {} is done with tasks({}/20):".format(name, tasks))
    for i in titles:
        print("\t {}".format(i))
