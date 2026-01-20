import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

DB_PATH = os.environ.get("DB_PATH", "/data/app.db")

app = Flask(__name__)

CORS(app)

def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)
        conn.commit()

init_db()

@app.get("/api/users")
def list_users():
    with get_conn() as conn:
        rows = conn.execute("SELECT id, username, password FROM users").fetchall()
        return jsonify([dict(r) for r in rows])

@app.get("/api/users/<int:user_id>")
def get_user(user_id):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, password FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

        if not row:
            return jsonify(error="Utilisateur introuvable"), 404

        return jsonify(dict(row))

@app.post("/api/users")
def create_user():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()

        return jsonify(id=cur.lastrowid, username=username, password=password), 201

@app.put("/api/users/<int:user_id>")
def update_user(user_id):
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    with get_conn() as conn:
        cur = conn.execute(
            "UPDATE users SET username = ?, password = ? WHERE id = ?",
            (username, password, user_id),
        )
        conn.commit()

        if cur.rowcount == 0:
            return jsonify(error="Utilisateur introuvable"), 404

    return jsonify(id=user_id, username=username, password=password)

@app.delete("/api/users/<int:user_id>")
def delete_user(user_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

        if cur.rowcount == 0:
            return jsonify(error="Utilisateur introuvable"), 404

    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)