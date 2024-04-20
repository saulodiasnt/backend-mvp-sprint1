from flask import g
from flask_openapi3 import APIBlueprint, Tag
from app.services.task_service import TaskService
from app.schemas import (
    CreateTaskSchema,
    UpdateTaskSchema,
    TaskPathSchema,
    TaskResponseSchema,
)
from app.shared.erros import NotFoundException, UnauthorizedException
from app.models.task import TaskType
from flask_cors import CORS
from flask import jsonify

security = [{"jwt": []}]

task_tag = Tag(name="Tasks", description="Task operations")
task_bp = APIBlueprint(
    "task",
    __name__,
    url_prefix="/tasks",
    abp_security=security,
    abp_tags=[task_tag],
    abp_responses={404: NotFoundException, 401: UnauthorizedException},
)

@task_bp.post("/", tags=[task_tag], responses={201: TaskResponseSchema})
def create_task(body: CreateTaskSchema):
    user_id = g.get("current_user").id
    
    task = TaskService.create_user_task(
        title=body.title,
        description=body.description,
        user_id=user_id,
        date=body.date,
        start_time=body.start_time,
        end_time=body.end_time,
        type=body.type,
    )

    return jsonify(task.to_dict()), 201


@task_bp.get("/", responses={200: TaskResponseSchema})
def list_tasks():
    user_id = g.get("current_user").id
    tasks = TaskService.get_all_user_task(user_id)
    return jsonify([task.to_dict() for task in tasks]), 200


@task_bp.get("/<int:task_id>", responses={200: TaskResponseSchema})
def get_task(path: TaskPathSchema):
    user_id = g.get("current_user").id
    task_id = path.task_id

    task = TaskService.get_user_task_by_id(task_id, user_id)
    if not task:
        return jsonify(error="Task not found"), 404

    return jsonify(task.to_dict()), 200


@task_bp.put("/<int:task_id>", responses={200: TaskResponseSchema})
def update_task(path: TaskPathSchema, body: UpdateTaskSchema):
    user_id = g.get("current_user").id
    task_id = int(path.task_id)
    print(body.type)
    task = TaskService.update_user_task(
        task_id=task_id,
        user_id=user_id,
        title=body.title,
        description=body.description,
        date=body.date,
        start_time=body.start_time,
        end_time=body.end_time,
        type=body.type,
    )

    if not task:
        return jsonify(error="Task not found"), 404

    return jsonify(task.to_dict()), 200


@task_bp.delete("/<int:task_id>", responses={204: None})
def delete_task(path: TaskPathSchema):
    user_id = g.get("current_user").id
    task_id = int(path.task_id)
    return TaskService.delete_user_task(task_id, user_id)
