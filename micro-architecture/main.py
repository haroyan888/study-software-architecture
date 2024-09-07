from flask import Flask
from dotenv import load_dotenv
from os import environ

import user
import todo


app = Flask(__name__)
app.register_blueprint(user.user_app)
app.register_blueprint(todo.todo_app)


if __name__ == '__main__':
	load_dotenv()

	app.run(
		host=environ.get('APP_HOST'),
		port=environ.get('APP_PORT'),
		debug=environ.get('APP_DEBUG')
	)
