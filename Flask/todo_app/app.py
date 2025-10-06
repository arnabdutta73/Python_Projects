from flask import Flask, jsonify, request
import json
import os

app = Flask("todo")
TODO_FILE = "todos.json"

# Load existing todos from file if it exists
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, "r") as f:
        try:
            todos = json.load(f)
        except json.JSONDecodeError:
            todos = []
else:
    todos = []

# Helper to save todos to file
def save_todos():
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)
# CRUD Operations for a simple To-Do application

# CREATE
@app.post('/todos')
def create_todo():
    data = request.get_json()
    todo = {"id": len(todos) + 1, "task": data["task"], "done": False}
    todos.append(todo)
    save_todos()
    return jsonify(todo), 201

# READ all
@app.get("/todos")
def get_todos():
    return jsonify(todos)

# READ one
@app.get("/todos/<int:todo_id>")
def get_todo(todo_id):
    todos_by_id = {t["id"]: t for t in todos}
    todo = todos_by_id.get(todo_id)
    if not todo:
        return jsonify({"error": "Not found"}), 404
    return jsonify(todo)

# UPDATE
@app.put("/todos/<int:todo_id>")
def update_todo(todo_id):
    data = request.get_json() or {}
    for t in todos:
        if t["id"] == todo_id:
            t["task"] = data.get("task", t["task"])
            t["done"] = data.get("done", t["done"])
            save_todos()
            return jsonify(t), 200
    return jsonify({"error": "Not found"}), 404

# DELETE
@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        todos.remove(todo)
        return jsonify({"message": "Deleted"}), 200
    save_todos()
    return jsonify({"error": "Not found"}), 404