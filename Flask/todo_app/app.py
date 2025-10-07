from flask import Flask, abort, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask("todo")
# SQLite DB file in project folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(512), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task, "done": self.done}

# create DB tables
with app.app_context():
    db.create_all()

def validate_todo_payload(data, partial=False):
    if not data or not isinstance(data, dict):
        return False, "JSON body required"
    if not partial:
        task = data.get("task")
        if not task or not isinstance(task, str) or not task.strip():
            return False, "Field 'task' is required and must be a non-empty string"
    if "done" in data and not isinstance(data["done"], bool):
        return False, "Field 'done' must be a boolean"
    return True, None

# JSON error handlers
@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({"error": "Bad Request", "message": getattr(e, "description", "")}), 400)

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"error": "Not Found", "message": getattr(e, "description", "")}), 404)

@app.errorhandler(500)
def server_error(e):
    return make_response(jsonify({"error": "Internal Server Error"}), 500)

# CRUD Operations for a simple To-Do application

# CREATE
@app.post('/todos')
def create_todo():
    if not request.is_json:
        abort(400, description="Expected application/json")
    data = request.get_json()
    ok, msg = validate_todo_payload(data)
    if not ok:
        abort(400, description=msg)
    todo = Todo(task=data["task"].strip(), done=False)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

# READ all
@app.get("/todos")
def get_todos():
    todos = [t.to_dict() for t in Todo.query.order_by(Todo.id).all()]
    return jsonify(todos), 200

# READ one
@app.get("/todos/<int:todo_id>")
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404, description=f"Todo with id {todo_id} not found")
    return jsonify(todo.to_dict()), 200

# UPDATE
@app.put("/todos/<int:todo_id>")
def update_todo(todo_id):
    if not request.is_json:
        abort(400, description="Expected application/json")
    data = request.get_json() or {}
    ok, msg = validate_todo_payload(data, partial=True)
    if not ok:
        abort(400, description=msg)
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404, description=f"Todo with id {todo_id} not found")
    if "task" in data:
        todo.task = data.get("task", todo.task).strip()
    if "done" in data:
        todo.done = data.get("done", todo.done)
    db.session.commit()
    return jsonify(todo.to_dict()), 200

# DELETE
@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404, description=f"Todo with id {todo_id} not found")
    db.session.delete(todo)
    db.session.commit()
    return "", 204