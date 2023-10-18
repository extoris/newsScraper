from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMIN = env.str("ADMIN")  # Тут у нас будет список из админов
DATABASE_NAME = env.str("DATABASE_NAME")
