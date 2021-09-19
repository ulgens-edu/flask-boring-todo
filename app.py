from datetime import datetime

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(length=200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        todos = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", todos=todos)

    elif request.method == "POST":
        content = request.form["content"]
        new_todo = Todo(content=content)

        db.session.add(new_todo)
        db.session.commit()

        return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return redirect("/")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    todo = Todo.query.get_or_404(id)

    if request.method == "GET":
        return render_template("update.html", todo=todo)

    elif request.method == "POST":
        todo.content = request.form["content"]
        db.session.commit()

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
