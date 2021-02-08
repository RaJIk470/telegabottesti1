import sqlite3

class Message:
	def __init__(self, database_file):
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS messages(message_id int, str text, user_id int, chat_id int)")
	def add_user(self, message_id, str, user_id, chat_id):
		with self.connection:
			if self.cursor.execute("SELECT * FROM messages WHERE user_id = '{}'".format(user_id)).fetchall() == []:
				return self.cursor.execute("INSERT INTO messages('first', 'last', 'username', 'user_id') VALUES('{}', '{}', '{}', '{}')".format(first, last, username, user_id))

	def get_table(self):
		with self.connection:
			messages = self.cursor.execute("SELECT * FROM messages").fetchall()
		return messages

	def recreate_table(self):
		self.cursor.execute("DROP TABLE IF EXISTS messages")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS messages(first text, last text, username text, user_id int)")

	def close(self):
		self.connection.commit()
		self.connection.close()