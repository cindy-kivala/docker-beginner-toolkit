from flask import Flask, request, jsonify
import os
from datetime import datetime
import json
import redis
from pathlib import Path

app = Flask(__name__)

try:
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
    redis_available = True
except:
    redis_available = False

tasks = []

# Configuration from environment
APP_TITLE = os.getenv('APP_TITLE', 'Docker Multi-Container Platform')
APP_AUTHOR = os.getenv('APP_AUTHOR', 'Moringa Student')

@app.route('/')
def home():
    if redis_available:
        visits = redis_client.incr('visitor_count')
    else:
        visits = "N/A"

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = os.uname().nodename
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_TITLE}</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
                max-width: 900px;
                width: 100%;
            }}
            h1 {{
                font-size: 3em;
                margin: 20px 0;
                color: white;
                text-align: center;
            }}
            .emoji {{
                font-size: 5em;
                text-align: center;
                animation: bounce 2s infinite;
            }}
            @keyframes bounce {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-20px); }}
            }}
            .badges {{
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 15px;
                margin: 30px 0;
            }}
            .badge {{
                background: rgba(255, 255, 255, 0.2);
                padding: 15px 25px;
                border-radius: 25px;
                color: white;
                font-size: 1.1em;
                animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
                0%, 100% {{ opacity: 1; transform: scale(1); }}
                50% {{ opacity: 0.8; transform: scale(1.05); }}
            }}
            .info {{
                background: rgba(0, 0, 0, 0.2);
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                color: white;
            }}
            .info p {{
                margin: 10px 0;
                font-size: 1.1em;
            }}
            .features {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 30px 0;
            }}
            .feature {{
                background: rgba(255, 255, 255, 0.15);
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                color: white;
            }}
            
            /* PROMINENT TASK MANAGER BUTTON */
            .task-manager-cta {{
                margin: 40px 0;
                text-align: center;
            }}
            .task-btn {{
                display: inline-block;
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                text-decoration: none;
                padding: 25px 50px;
                border-radius: 50px;
                font-size: 1.5em;
                font-weight: bold;
                box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
                transition: all 0.3s ease;
                animation: glow 2s infinite;
            }}
            .task-btn:hover {{
                transform: translateY(-5px) scale(1.05);
                box-shadow: 0 15px 40px rgba(245, 87, 108, 0.6);
            }}
            @keyframes glow {{
                0%, 100% {{ box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4); }}
                50% {{ box-shadow: 0 10px 40px rgba(245, 87, 108, 0.8); }}
            }}
            
            .api-section {{
                margin-top: 30px;
                padding: 20px;
                background: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                color: white;
            }}
            .api-section h3 {{
                margin-bottom: 15px;
                font-size: 1.2em;
            }}
            .api-endpoint {{
                background: rgba(255, 255, 255, 0.1);
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                font-family: monospace;
                font-size: 0.9em;
            }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                color: rgba(255, 255, 255, 0.8);
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🐳</div>
            <h1>Docker Multi-Container Platform</h1>
            
            <div class="badges">
                <div class="badge">👥 Visitors: <strong>{visits}</strong></div>
                <div class="badge">🔴 Redis: <strong>{'✅' if redis_available else '❌'}</strong></div>
                <div class="badge">📝 Tasks: <strong>{len(tasks)}</strong></div>
            </div>
            
            <div class="info">
                <p>📅 <strong>Time:</strong> {current_time}</p>
                <p>🖥️ <strong>Container ID:</strong> {hostname}</p>
                <p>👤 <strong>Author:</strong> {APP_AUTHOR}</p>
            </div>
            
            <!-- PROMINENT CALL TO ACTION FOR TASK MANAGER -->
            <div class="task-manager-cta">
                <a href="/tasks" class="task-btn">
                    📝 Open Task Manager
                </a>
            </div>
            
            <div class="features">
                <div class="feature">
                    <h3>🎯 Multi-Container</h3>
                    <p>Flask + Redis orchestrated with Docker Compose</p>
                </div>
                <div class="feature">
                    <h3>🔄 Persistent Data</h3>
                    <p>Redis stores visitor count across restarts</p>
                </div>
                <div class="feature">
                    <h3>🌐 REST API</h3>
                    <p>Full CRUD endpoints for task management</p>
                </div>
                <div class="feature">
                    <h3>⚡ Real-Time</h3>
                    <p>Live visitor counter updates</p>
                </div>
            </div>
            
            <div class="api-section">
                <h3>🔌 API Endpoints:</h3>
                <div class="api-endpoint">GET /api/tasks - List all tasks</div>
                <div class="api-endpoint">POST /api/tasks - Create new task</div>
                <div class="api-endpoint">DELETE /api/tasks/&lt;id&gt; - Delete task</div>
                <div class="api-endpoint">GET /api/stats - Container statistics</div>
                <div class="api-endpoint">GET /health - Health check</div>
                <div class="api-endpoint">GET /reset - Reset visitor counter</div>
            </div>
            
            <div class="footer">
                <p>Moringa School AI Capstone Project</p>
                <p>Built with Flask, Docker, Redis & Passion</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({
        'tasks': tasks,
        'count': len(tasks),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title required'}), 400
    
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

@app.route('/api/stats')
def stats():
    """Container statistics"""
    return jsonify({
        'container_id': os.uname().nodename,
        'uptime': datetime.now().isoformat(),
        'total_tasks': len(tasks),
        'python_version': os.sys.version,
        'environment': 'Docker Container'
    })

@app.route('/health')
def health():
    return {
        'status': 'healthy', 
        'redis': 'connected' if redis_available else 'disconnected',
        'message': 'Docker container is running!'
    }, 200

@app.route('/reset')
def reset():
    if redis_available:
        redis_client.set('visitor_count', 0)
        return {'message': 'Counter reset!', 'count': 0}, 200
    return {'error': 'Redis not available'}, 500


@app.route('/tasks')
def tasks_page():
    """Web interface for managing tasks"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Task Manager</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #667eea;
                margin-bottom: 30px;
                text-align: center;
            }
            .back-link {
                display: inline-block;
                margin-bottom: 20px;
                color: #667eea;
                text-decoration: none;
                font-weight: bold;
            }
            .back-link:hover { text-decoration: underline; }
            .task-form {
                background: #f8f9fa;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 30px;
            }
            .input-group {
                display: flex;
                gap: 10px;
            }
            input[type="text"] {
                flex: 1;
                padding: 12px;
                font-size: 16px;
                border: 2px solid #ddd;
                border-radius: 8px;
                transition: border 0.3s;
            }
            input[type="text"]:focus {
                outline: none;
                border-color: #667eea;
            }
            button {
                padding: 12px 30px;
                font-size: 16px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s;
            }
            button:hover {
                background: #5568d3;
            }
            .task-list {
                list-style: none;
            }
            .task-item {
                background: white;
                padding: 20px;
                margin-bottom: 15px;
                border-radius: 10px;
                border-left: 4px solid #667eea;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            }
            .task-item:hover {
                transform: translateX(5px);
            }
            .task-content {
                flex: 1;
            }
            .task-title {
                font-size: 1.1em;
                color: #333;
                margin-bottom: 5px;
            }
            .task-meta {
                font-size: 0.85em;
                color: #666;
            }
            .delete-btn {
                padding: 8px 20px;
                background: #dc3545;
                font-size: 14px;
            }
            .delete-btn:hover {
                background: #c82333;
            }
            .no-tasks {
                text-align: center;
                padding: 40px;
                color: #666;
                font-style: italic;
            }
            .task-count {
                text-align: center;
                margin-bottom: 20px;
                color: #667eea;
                font-weight: bold;
                font-size: 1.2em;
            }
            .success-message {
                background: #d4edda;
                color: #155724;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-link">← Back to Home</a>
            <h1>Task Manager</h1>
            
            <div id="successMessage" class="success-message"></div>
            
            <div class="task-form">
                <div class="input-group">
                    <input type="text" id="taskInput" placeholder="Enter a new task..." />
                    <button onclick="addTask()">Add Task</button>
                </div>
            </div>
            
            <div class="task-count" id="taskCount">Loading tasks...</div>
            
            <ul class="task-list" id="taskList">
                <li class="no-tasks">Loading...</li>
            </ul>
        </div>

        <script>
            // Load tasks on page load
            loadTasks();

            // Add task with Enter key
            document.getElementById('taskInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    addTask();
                }
            });

            function loadTasks() {
                fetch('/api/tasks')
                    .then(response => response.json())
                    .then(data => {
                        const taskList = document.getElementById('taskList');
                        const taskCount = document.getElementById('taskCount');
                        
                        taskCount.textContent = `Total Tasks: ${data.count}`;
                        
                        if (data.tasks.length === 0) {
                            taskList.innerHTML = '<li class="no-tasks">No tasks yet. Add one above! 🚀</li>';
                        } else {
                            taskList.innerHTML = data.tasks.map(task => `
                                <li class="task-item">
                                    <div class="task-content">
                                        <div class="task-title">${task.title}</div>
                                        <div class="task-meta">
                                            ID: ${task.id} | Created: ${new Date(task.created_at).toLocaleString()}
                                        </div>
                                    </div>
                                    <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
                                </li>
                            `).join('');
                        }
                    })
                    .catch(error => {
                        console.error('Error loading tasks:', error);
                        document.getElementById('taskList').innerHTML = 
                            '<li class="no-tasks">Error loading tasks</li>';
                    });
            }

            function addTask() {
                const input = document.getElementById('taskInput');
                const title = input.value.trim();
                
                if (!title) {
                    alert('Please enter a task title');
                    return;
                }

                fetch('/api/tasks', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ title: title })
                })
                .then(response => response.json())
                .then(data => {
                    input.value = '';
                    showSuccess('Task added successfully! ✅');
                    loadTasks();
                })
                .catch(error => {
                    console.error('Error adding task:', error);
                    alert('Error adding task');
                });
            }

            function deleteTask(taskId) {
                if (!confirm('Are you sure you want to delete this task?')) {
                    return;
                }

                fetch(`/api/tasks/${taskId}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    showSuccess('Task deleted successfully! 🗑️');
                    loadTasks();
                })
                .catch(error => {
                    console.error('Error deleting task:', error);
                    alert('Error deleting task');
                });
            }

            function showSuccess(message) {
                const successMsg = document.getElementById('successMessage');
                successMsg.textContent = message;
                successMsg.style.display = 'block';
                setTimeout(() => {
                    successMsg.style.display = 'none';
                }, 3000);
            }
        </script>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)