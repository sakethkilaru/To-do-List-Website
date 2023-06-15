from flask import Blueprint, render_template, redirect, url_for, request

from todoapp.extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo_item = request.form.get('add-todo')
    todos_collection.insert_one({'text': todo_item, 'complete': False})
    return redirect(url_for('main.index'))
