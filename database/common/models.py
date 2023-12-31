import datetime

from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField, TextField, DateTimeField

db = SqliteDatabase('database/peewee_orm.db')


class BaseModel(Model):
	"""
	Базовая модель для всех таблиц.
	"""
	class Meta:
		"""
		Добавляется связь с БД.
		"""
		database = db


class User(BaseModel):
	"""
	Модель пользователя.
	"""
	name = CharField()
	telegram_id = IntegerField()


class Currency(BaseModel):
	"""
	Модель валют привязанных к пользователю.
	"""
	owner = ForeignKeyField(User, backref='currencies')
	name = CharField()


class History(BaseModel):
	"""
	История запросов пользователя.
	"""
	user = ForeignKeyField(User, backref='history')
	text = TextField()
	created = DateTimeField(default=datetime.datetime.now())
