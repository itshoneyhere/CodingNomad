'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
import pprint as p

res = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
print("------------")
print("------------")
data = res.json()["data"]
result =[i["email"] for i in data]
print(result)
