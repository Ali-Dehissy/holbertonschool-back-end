#!/usr/bin/python3
"""Returns a TO DO list for a given employe ID"""

import sys
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()

    nameFile = str(eval(sys.argv[1])) + ".csv"

    j = open(nameFile, "x")
    for task in todos:
        s = (
            '"'
            + str(user.get("id"))
            + '","'
            + str(user.get("username"))
            + '","'
            + str(task.get("completed"))
            + '","'
            + str(task.get("title"))
            + '"\n'
        )
        j.write(s)

