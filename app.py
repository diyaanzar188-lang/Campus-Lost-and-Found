from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "lostfoundsecret"

# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect("lostfound.db")

with get_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            contact TEXT,
            status TEXT
        )
    """)

# ---------- HOME ----------
@app.route("/")
def home():
    return redirect("/login")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        regno = request.form["regno"].strip()
        password = request.form["password"].strip()

        if not regno.startswith("LBT") or len(regno) < 9:
            error = "Invalid Register Number"
        else:
            expected_password = "lbt" + regno[-3:]
            if password == expected_password:
                session["user"] = regno
                return redirect("/dashboard")
            else:
                error = "Wrong Password"

    return render_template("login.html", error=error)

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    with get_db() as db:
        lost_items = db.execute(
            "SELECT id, name, description, contact, status FROM items WHERE status='Lost'"
        ).fetchall()

        found_items = db.execute(
            "SELECT id, name, description, contact, status FROM items WHERE status='Found'"
        ).fetchall()

        recovered_items = db.execute(
            "SELECT id, name, description, contact, status FROM items WHERE status='Recovered'"
        ).fetchall()

    return render_template(
        "index.html",
        lost_items=lost_items,
        found_items=found_items,
        recovered_items=recovered_items
    )

# ---------- ADD ITEM ----------
@app.route("/add", methods=["POST"])
def add_item():
    name = request.form["name"]
    description = request.form["description"]
    contact = request.form["contact"]
    status = request.form["status"]

    with get_db() as db:
        db.execute(
            "INSERT INTO items (name, description, contact, status) VALUES (?, ?, ?, ?)",
            (name, description, contact, status)
        )

    return redirect("/dashboard")
# ---------- MARK FOUND ----------
@app.route("/mark_found/<int:item_id>", methods=["POST"])
def mark_found(item_id):
    with get_db() as db:
        db.execute(
            "UPDATE items SET status='Found' WHERE id=?",
            (item_id,)
        )
    return redirect("/dashboard")

# ---------- RECOVER ----------
@app.route("/recover/<int:item_id>")
def recover(item_id):
    with get_db() as db:
        db.execute("UPDATE items SET status='Recovered' WHERE id=?", (item_id,))
    return redirect("/dashboard")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)