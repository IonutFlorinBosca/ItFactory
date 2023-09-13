# ca sa putem sa scriem rutele in fisiere diferite vom folosi un concept numit
# BLUEPRINT
# acel blueprint va actiona ca o semi-aplicatie(o aplicatie intr-o aplicatie)
# care se va referi doar la tasks

from flask import Blueprint, abort, jsonify, request, Response
from repository import tasks as tasks_repo

bp = Blueprint("tasks", __name__, url_prefix="/tasks")
print(bp)
print(tasks_repo)


@bp.route("/")
def get_all():
    tasks = tasks_repo.get_tasks()
    print(tasks)
    if not tasks:
        abort(404)
    return jsonify(tasks)


@bp.route("/", methods=["POST"])
def add_task():
    task_data = request.json
    tasks_repo.add_task(task_data)
    return Response("OK", 201)


@bp.route("/<title>", methods=["PATCH"])
def update_task(title):
    task_data = request.json
    tasks_repo.update_task(title, task_data)
    return Response("OK", 200)


@bp.route("/<title>", methods=["DELETE"])
def delete_task(title):
    tasks_repo.delete_task(title)
    return Response("OK", 200)
