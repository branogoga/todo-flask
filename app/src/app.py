import uuid

from flask import Flask, render_template, redirect, url_for

from data.model.orm import create_db_session
from data.model.task import Task

app = Flask(__name__)


@app.route('/')
def list():
    with create_db_session() as session:
        tasks = session.query(Task).order_by(Task.id).limit(10).all()
        return render_template('list.html', tasks=tasks)


@app.route('/add')
def add():
    with create_db_session() as session:
        task = Task(title=f"Title {uuid.uuid4()}", description=f"Description {uuid.uuid4()}")
        session.add(task)
        session.commit()
        return redirect(url_for('list'), code=302)


@app.route('/remove/<task_id>')
def remove(task_id: int):
    with create_db_session() as session:
        task = session.query(Task).get(task_id)
        session.delete(task)
        session.commit()
    return redirect(url_for('list'), code=302)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
