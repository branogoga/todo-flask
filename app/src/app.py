from data.model.orm import get_version, get_db_time
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def tasks():
    return render_template('tasks.html', sqlalchemy_version=get_version(), time=get_db_time())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
