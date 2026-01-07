from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


#Pydantic model
class task(BaseModel):
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
        "id" :1,
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


#Read a single task

#Read all the tasks

#Update task

#Delete tasks