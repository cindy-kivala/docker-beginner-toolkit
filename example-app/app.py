from flask import Flask, request, jsonify
import os
from datetime import datetime
import json
import redis
from pathlib import Path
import psutil

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
            .api-section {{
                margin-top: 30px;
                padding: 20px;
                background: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                color: white;
            }}
            .api-endpoint {{
                background: rgba(255, 255, 255, 0.1);
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                font-family: monospace;
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
                <h3>🔌 Available API Endpoints:</h3>
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


# @app.route('/api/system')
# def system_info():
#     """Get system information"""
#     return jsonify({
#         'cpu_percent': psutil.cpu_percent(interval=1),
#         'memory': {
#             'total': psutil.virtual_memory().total,
#             'available': psutil.virtual_memory().available,
#             'percent': psutil.virtual_memory().percent
#         },
#         'disk': {
#             'total': psutil.disk_usage('/').total,
#             'used': psutil.disk_usage('/').used,
#             'percent': psutil.disk_usage('/').percent
#         },
#         'container_id': os.uname().nodename
#     })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)