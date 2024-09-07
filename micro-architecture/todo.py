from flask import jsonify, Blueprint
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, Boolean

from repos import repos


todo_app = Blueprint('todo', __name__)


# Todoテーブル
class Todo(repos.Base):
	__tablename__ = "todo"
	todo_id = Column(Integer, primary_key=True)
	title = Column(String(255))
	description = Column(Text)
	completion = Column(Boolean, default=False)

	def create_table():
		repos.Base.metadata.create_all(repos.engine, checkfirst=False, tables=[Todo.__table__])

	def to_json(self):
		return jsonify({
			"todo_id": self.todo_id,
			"title": self.title,
			"description": self.description,
			"completion": self.completion,
		})


@todo_app.route('/todo')
def add_todo():
	session = repos.create_session()
	todo = Todo(title="Test Todo", description="Todo description")
	session.add(todo)
	session.commit()

	return todo.to_json(), 200
