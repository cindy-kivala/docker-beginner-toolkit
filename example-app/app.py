from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

try:
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
    redis_available = True
except:
    redis_available = False

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
        <title>Docker Multi-Container Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
            }}
            h1 {{ font-size: 3em; margin: 0; }}
            .emoji {{ font-size: 4em; animation: bounce 2s infinite; }}
            @keyframes bounce {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-20px); }}
            }}
            .info {{ 
                background: rgba(0, 0, 0, 0.2);
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }}
            .badge {{
                display: inline-block;
                background: rgba(255, 255, 255, 0.2);
                padding: 10px 20px;
                border-radius: 20px;
                margin: 10px 5px;
                font-size: 1.2em;
                animation: pulse 2s infinite;
            }}
            @keyframes pulse {{
                0%, 100% {{ opacity: 1; }}
                50% {{ opacity: 0.7; }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🐳</div>
            <h1>Multi-Container Docker App!</h1>
            <p style="font-size: 1.2em;">Flask + Redis running in separate containers</p>
            
            <div class="badge">
                👥 Visitors: <strong>{visits}</strong>
            </div>
            
            <div class="info">
                <p>📅 <strong>Time:</strong> {current_time}</p>
                <p>🖥️ <strong>Container ID:</strong> {hostname}</p>
                <p>🔴 <strong>Redis Status:</strong> {'Connected ✅' if redis_available else 'Disconnected ❌'}</p>
            </div>
            
            <p style="margin-top: 30px; font-size: 0.9em;">
                🎉 This demonstrates Docker Compose orchestrating multiple containers!
            </p>
        </div>
    </body>
    </html>
    """
    return html

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)