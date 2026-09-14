import os
import socket
from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis = Redis(host=redis_host, port=6379, socket_timeout=2)


@app.route("/api/health")
def health():
    return jsonify(status="UP", hostname=socket.gethostname())


@app.route("/api/data")
def data():
    try:
        count = redis.incr("hits")
    except Exception:
        count = "No Redis connection"

    return jsonify(
        message="Hello from the backend microservice (managed by uv)!",
        hostname=socket.gethostname(),
        visits=count,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
