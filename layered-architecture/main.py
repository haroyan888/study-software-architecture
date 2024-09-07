# アプリケーション層
from flask import Flask
from dotenv import load_dotenv
from os import environ

from router import router


app = Flask(__name__)
app.register_blueprint(router)


if __name__ == '__main__':
	load_dotenv()

	app.run(
		host=environ.get('APP_HOST'),
		port=environ.get('APP_PORT'),
		debug=environ.get('APP_DEBUG')
	)
