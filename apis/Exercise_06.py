'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.
'''

import requests

input_prompt='''Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)
'''

inp=input(input_prompt).split(" ")
print(type(inp))
task_id=0
for i in inp:
    print(i)
    i = int(i)

    match i:
        case 1:
            from Exercise_03 import created_id
        case 2:
            res =requests.get("http://demo.codingnomads.co:8080/tasks_api/tasks",params={"userId":created_id})
            print(res.text)

        case 3:
            res =requests.get("http://demo.codingnomads.co:8080/tasks_api/tasks",params={"userId":created_id,"completed":True})
            print(res.text)
        case 4:
            res =requests.get("http://demo.codingnomads.co:8080/tasks_api/tasks",params={"userId":created_id,"completed":False})
            print(res.text)
        case 5:
            payload = {
                "userId": created_id,
                "name": "task created",
                "description": "this task was created in case 5",
                "completed": False
                    }
            response = requests.post("http://demo.codingnomads.co:8080/tasks_api/tasks",json=payload)
            task_id= response.json()["data"]["id"]
            print(response.text)
        case 6:
            payload={
                "name": "task updated",
                "description": "this task was updates in case 6",
                "completed": True}
            response = requests.patch("http://demo.codingnomads.co:8080/tasks_api/tasks",params={"userId":created_id},json=payload)
            print(response.text)
        case 7:
            res= requests.delete("http://demo.codingnomads.co:8080/tasks_api/tasks",params={"id":task_id})
            print(res.text)

        
        
