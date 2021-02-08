class User:
	def __init__(self, first, last, user_id, username):
		self.first = first
		self.last = last
		self.user_id = user_id
		self.username = username

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	@fullname.setter
	def fullname(self, fullname):
		self.first, self.last = fullname.split()