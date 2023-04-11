'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.
'''
import requests
import random
from Exercise_03 import created_id as old_id

email="Mrdo"+str(random.randint(0,10000))+"m@gmail.com"
data ={"email":email,"first_name":"Ding Ding","last_name":"Dong Dong"}

res = requests.put("http://demo.codingnomads.co:8080/tasks_api/users/"+str(old_id),json=data)

res_get = requests.get("http://demo.codingnomads.co:8080/tasks_api/users/"+str(old_id))
print(res_get.text)



