'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.
'''
import requests
import random

email="Mrdo"+str(random.randint(0,10000))+"m@gmail.com"
data ={"email":email,"first_name":"Mr","last_name":"Doodle"}

res = requests.post("http://demo.codingnomads.co:8080/tasks_api/users",json=data)

created_id = res.json()["data"]["id"]

res_get = requests.get("http://demo.codingnomads.co:8080/tasks_api/users/"+str(created_id))
print(res_get.text)

