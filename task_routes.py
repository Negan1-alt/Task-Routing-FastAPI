from fastapi import APIRouter, HTTPException
from task_schemas import CreateTask, UpdateTaskStatus

router = APIRouter(prefix = "/tasks", tags = ["Tasks"])

tasks = [
    {"id":1, "title":"Fix Login Bug", "done":False},
    {"id":2, "title":"Write API Docs", "done":False}
    ]

@router.get("")
def get_tasks(search:str = None):
    if search is None:
        return tasks

    result = [task for task in tasks if search.lower() in task["title"].lower()]
    return result            

@router.get("/{task_id}")
def get_router_by_id(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code = 404, detail = "task Not Found")  

@router.post("", status_code = 201)
def create_task(data:CreateTask):
    new_id = 1

    for task in tasks:
        if task["id"] >= new_id:
            new_id = task["id"] + 1

    new_task = {"id": new_id, "title":data.title, "done":data.done}
    tasks.append(new_task)  
    return new_task

@router.put("/{task_id}")
def modify_all_task_info(task_id:int, data:CreateTask):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.title
            task["done"] = data.done
            return task
    raise HTTPException(status_code = 404, detail = "Task Not Found")

@router.patch("/{task_id}")
def modify_task_status(task_id:int, data:UpdateTaskStatus):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = data.done
            return task
    raise HTTPException(status_code = 404,detail = "Task not found")

@router.delete("/{task_id}")
def delete_task_by_id(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": f"Task {task} has been deleted"}
    raise HTTPException(status_code = 404,detail = "Task not Found")
        