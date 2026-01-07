from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
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
@app.post("/tasks",status_code=status.HTTP_201_CREATED)
def create_tasks(task : Task):
    data.append(task.model_dump())
    return {"message" : "task has been created"}
#Read a single task
@app.get("/tasks/{id}")
def list_single_task(id : int):
    for task in data:
        if task["id"] == id:
            return {"detail" : task}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")

#Read all the tasks

@app.get("/tasks")
def get_all_tasks(): 
    return {"detail" : data }
#Update task
@app.put("/tasks/{id}", status_code=status.HTTP_200_OK)
def update_task(id : int, task: Task):
    for item in data:
        if item["id"] == id:
            item.update(task.model_dump())
            
            return {"message" : "updated task",
                    "task" : item}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#Delete tasks
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id : int):
    for i, item in enumerate(data):
        if item["id"] == id:
            data.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="task don't exist")
