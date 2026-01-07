from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


#Pydantic model
class Task(BaseModel):
    id : int
    title : str
    description : str | None = None
    completed : bool = True

#Task data
data = [
    {
        "id" :1,
        "title" : "complete fastapi course",
        "description" : None,
        "completed" : True ,
    },
    {
        "id" :2,
        "title" : "buy the groceries",
        "description" : "yams, eggs, beans",
        "completed" : False,
    },
    {
        "id" :3,
        "title" : "Finish this project",
        # "description" : None,
        # "completed" : True ,
    },
]

#Home page endpoint
@app.get("/")
def welcome():
    return {"message" : "Welcome to my todo-list app"}
# Create task endpoint
@app.post("/tasks")
def create_tasks(task : Task):
    data.append(task)
    return {"message" : "task has been created"}
#Read a single task


#Read all the tasks

@app.get("/tasks")
def get_all_tasks(): 
    return {"detail" : data }
#Update task

#Delete tasks