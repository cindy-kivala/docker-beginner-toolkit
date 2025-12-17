from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = os.uname().nodename
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
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
            }}
            h1 {{ font-size: 3em; margin: 0; }}
            .emoji {{ font-size: 4em; }}
            .info {{ 
                background: rgba(0, 0, 0, 0.2);
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🐳</div>
            <h1>Hello from Docker!</h1>
            <p style="font-size: 1.2em;">This Flask app is running inside a Docker container</p>
            <div class="info">
                <p>📅 <strong>Time:</strong> {current_time}</p>
                <p>🖥️ <strong>Hostname:</strong> {hostname}</p>
                <p>✅ <strong>Status:</strong> Container is running successfully!</p>
            </div>
            <p style="margin-top: 30px; font-size: 0.9em;">
                🎉 If you can see this, you've successfully Dockerized your first app!
            </p>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Docker container is running!'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)