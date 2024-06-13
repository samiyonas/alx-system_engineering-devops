#!/usr/bin/python3
""" gather data from an API """
import json
import requests
from sys import argv


if __name__ == "__main__":
    res_1 = requests.get("https://jsonplaceholder.typicode.com/users")
    res_2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    res_1 = res_1.json()
    res_2 = res_2.json()

    Id = int(argv[1])
    name = res_1[Id - 1].get("username")
    user_list = []

    for i in range((Id - 1) * 20, ((Id - 1) * 20) + 20):
        userId = res_2[i].get("userId")
        dct = {}
        dct["task"] = res_2[i].get("title")
        dct["completed"] = res_2[i].get("completed")
        dct["username"] = name
        user_list.append(dct)
    final_json = {str(userId): user_list}
    with open("{}.json".format(userId), 'w') as f:
        json.dump(final_json, f)
