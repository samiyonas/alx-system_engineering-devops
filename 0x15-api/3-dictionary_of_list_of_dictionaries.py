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

    user_list = []

    x = 0
    y = 20
    fdct = {}
    flist = []
    for i in res_1:
        for j in res_2[x:y]:
            j["username"] = i.get("username")
        x = x + 20
        y = y + 20

    for k in res_2:
        dct = {}
        dct["username"] = k["username"]
        dct["task"] = k["title"]
        dct["completed"] = k["completed"]
        dct["userId"] = k["userId"]
        user_list.append(dct)
    for l in range(1, 11):
        for m in user_list:
            if m["userId"] == l:
                flist.append(m)
            else:
                break
        fdct[str(l)] = flist

    with open("todo_all_employees.json", 'w') as f:
        json.dump(fdct, f)
