# ドメイン層
from sqlalchemy import create_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import jsonify


class Repository():
	def __init__(self, url: str):
		self.engine = create_engine(url)
		self.Base = declarative_base()
	
	def create_tables(self):
		self.Base.metadata.create_all(self.engine)

	def create_session(self):
		return sessionmaker(self.engine)()


# DBへ接続するエンジンを作成
repos = Repository("sqlite:///layered-system.sqlite")

# Userテーブル
class User(repos.Base):
	__tablename__ = "user"
	user_id = Column(Integer, primary_key=True)
	first_name = Column(String(255))
	last_name = Column(String(255))
	age = Column(Integer)

	def create(self):
		session = repos.create_session()
		session.add(self)
		session.commit()

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

	def create(self):
		session = repos.create_session()
		session.add(self)
		session.commit()

	def to_json(self):
		return jsonify({
			"todo_id": self.todo_id,
			"title": self.title,
			"description": self.description,
			"completion": self.completion,
		})