from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>High Availability Demo</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f4f6f8;
                color: #333;
                text-align: center;
                padding: 50px;
            }}
            .card {{
                background: #fff;
                border-radius: 12px;
                padding: 30px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #0073e6;
                font-size: 2.2em;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.1em;
                margin: 10px 0;
            }}
            .hostname {{
                font-weight: bold;
                color: #28a745;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 High Availability Demo</h1>
            <p>This app is running inside a container.</p>
            <p><span class="hostname">Server Hostname:</span> {hostname}</p>
        </div>
    </body>
    </html>
    """

@app.route("/api/health")
def health():
    return jsonify(status="UP", message="App is healthy 🚀")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
