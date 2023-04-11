'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.
'''

import requests
import random
from Exercise_04 import old_id


res = requests.delete("http://demo.codingnomads.co:8080/tasks_api/users/"+str(old_id))

res_get = requests.get("http://demo.codingnomads.co:8080/tasks_api/users/"+str(old_id))
get_data = res_get.json()
if(get_data["status"] == "200 OK" and get_data["data"] is None):
    print("Resource deleted")
