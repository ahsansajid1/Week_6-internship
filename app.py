from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

FILE = "notes.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def load_notes():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

@app.route("/")
def index():
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note")
    notes = load_notes()
    notes.append({"note": note})
    save_notes(notes)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword", "").lower()
    notes = load_notes()
    results = [n for n in notes if keyword in n["note"].lower()]
    return render_template("search.html", notes=results, keyword=keyword)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
