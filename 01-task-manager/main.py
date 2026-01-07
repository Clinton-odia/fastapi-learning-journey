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

# Create task endpoint


#Read a single task

#Read all the tasks

#Update task

#Delete tasks