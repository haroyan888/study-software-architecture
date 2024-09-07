from flask import Flask, jsonify
from dotenv import load_dotenv
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base


app = Flask(__name__)


class Repository():
	def __init__(self, url: str):
		self.engine = create_engine(url)
		self.Base = declarative_base()
	
	def create_tables(self):
		self.Base.metadata.create_all(self.engine)

	def create_session(self):
		return sessionmaker(self.engine)()


# DBへ接続するエンジンを作成
repos = Repository("sqlite:///monolithic-system.sqlite")

# Userテーブル
class User(repos.Base):
	__tablename__ = "user"
	user_id = Column(Integer, primary_key=True)
	first_name = Column(String(255))
	last_name = Column(String(255))
	age = Column(Integer)

	def to_json(self):
		return jsonify({
			"user_id": self.user_id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"age": self.age,
		})


# Todoテーブル
class Todo(repos.Base):
	__tablename__ = "todo"
	todo_id = Column(Integer, primary_key=True)
	title = Column(String(255))
	description = Column(Text)
	completion = Column(Boolean, default=False)

	def to_json(self):
		return jsonify({
			"todo_id": self.todo_id,
			"title": self.title,
			"description": self.description,
			"completion": self.completion,
		})


@app.route('/user')
def add_user():
	session = repos.create_session()
	user = User(first_name="Haruto", last_name="Yamazaki", age=20)
	session.add(user)
	session.commit()

	return user.to_json(), 200


@app.route('/todo')
def add_todo():
	session = repos.create_session()
	todo = Todo(title="Test Todo", description="Todo description")
	session.add(todo)
	session.commit()

	return todo.to_json(), 200


if __name__ == '__main__':
	load_dotenv()

	app.run(
		host=environ.get('APP_HOST'),
		port=environ.get('APP_PORT'),
		debug=environ.get('APP_DEBUG')
	)
