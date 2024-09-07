from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Repository():
	def __init__(self, url: str):
		self.engine = create_engine(url)
		self.Base = declarative_base()

	def create_session(self):
		return sessionmaker(self.engine)()


# DBへ接続するエンジンを作成
repos = Repository("sqlite:///micro-service-system.sqlite")