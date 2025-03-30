import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css"; // Ensure this has styles for .delete-button

const API_URL = "http://127.0.0.1:8000"; // Backend URL

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    axios.get(`${API_URL}/tasks`)
      .then(response => setTasks(response.data))
      .catch(error => console.error("Error fetching tasks:", error));
  }, []);

  const addTask = () => {
    if (!newTask.trim()) return; // Prevent empty tasks

    axios.post(`${API_URL}/tasks`, { title: newTask, completed: false })
      .then(response => {
        setTasks([...tasks, response.data]);
        setNewTask(""); // Clear input after adding
      })
      .catch(error => console.error("Error adding task:", error));
  };

  const handleCheckboxChange = (taskId) => {
    const task = tasks.find(task => task.id === taskId);
    const updatedStatus = !task.completed;

    axios.put(`${API_URL}/tasks/${taskId}`, { completed: updatedStatus })
      .then(() => {
        setTasks(tasks.map(task => 
          task.id === taskId ? { ...task, completed: updatedStatus } : task
        ));
      })
      .catch(error => console.error("Error updating task:", error));
  };

  const handleDelete = (taskId) => {
    axios.delete(`${API_URL}/tasks/${taskId}`)
      .then(() => {
        setTasks(tasks.filter(task => task.id !== taskId));
      })
      .catch(error => console.error("Error deleting task:", error));
  };

  return (
    <div className="card-container">
      <div className="card">
        <h1 className="card-header">To-Do List</h1>
        <ul className="card-list">
          {tasks.map(task => (
            <li key={task.id} className="task-item">
              <input 
                type="checkbox" 
                id={`task-${task.id}`} 
                onChange={() => handleCheckboxChange(task.id)} 
                checked={task.completed || false} 
              />
              <label htmlFor={`task-${task.id}`}>{task.title}</label>
              <button 
                className="delete-button"
                onClick={() => handleDelete(task.id)}
              >
                X
              </button>
            </li>
          ))}
        </ul>
        <input 
          type="text" 
          placeholder="Enter a new task..." 
          className="card-input" 
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
        />
        <button className="card-button" onClick={addTask}>
          Add Task
        </button>
      </div>
    </div>
  );
}

export default App;
