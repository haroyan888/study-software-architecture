from flask import jsonify, Blueprint
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from repos import repos


user_app = Blueprint('user', __name__)


# Userテーブル
class User(repos.Base):
	__tablename__ = "user"
	user_id = Column(Integer, primary_key=True)
	first_name = Column(String(255))
	last_name = Column(String(255))
	age = Column(Integer)

	def create_table():
		repos.Base.metadata.create_all(repos.engine, checkfirst=False, tables=[User.__table__])

	def to_json(self):
		return jsonify({
			"user_id": self.user_id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"age": self.age,
		})


@user_app.route('/user')
def add_user():
	session = repos.create_session()
	user = User(first_name="Haruto", last_name="Yamazaki", age=20)
	session.add(user)
	session.commit()

	return user.to_json(), 200