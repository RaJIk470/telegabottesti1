from config import *
import handlers
#database.recreate_table()


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)