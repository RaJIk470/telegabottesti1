import sqlite3

class Database:
	def __init__(self, database_file):
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS users(first text, last text, username text, user_id int)")
	def add_user(self, first, last, username, user_id):
		with self.connection:
			if self.cursor.execute("SELECT * FROM users WHERE user_id = '{}'".format(user_id)).fetchall() == []:
				return self.cursor.execute("INSERT INTO users('first', 'last', 'username', 'user_id') VALUES('{}', '{}', '{}', '{}')".format(first, last, username, user_id))

	def get_table(self):
		with self.connection:
			users = self.cursor.execute("SELECT * FROM users").fetchall()
		return users

	def recreate_table(self):
		self.cursor.execute("DROP TABLE IF EXISTS users")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS users(first text, last text, username text, user_id int)")

	def close(self):
		self.connection.commit()
		self.connection.close()