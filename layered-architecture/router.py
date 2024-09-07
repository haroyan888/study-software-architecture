# アプリケーション層
from flask import Blueprint

from repos import User, Todo


router = Blueprint("router", __name__)


@router.route('/user')
def add_user():
	# バリデーションとか
	user = User(first_name="Haruto", last_name="Yamazaki", age=20)
	user.create()

	return user.to_json(), 200


@router.route('/todo')
def add_todo():
	# バリデーションとか
	todo = Todo(title="Test Todo", description="Todo description")
	todo.create()

	return todo.to_json(), 200