from data import db_session
from data.users_model import User

db_name = input()

db_session.global_init(db_name)
session = db_session.create_session()


for user in session.query(User).filter(User.address == 'module_1'):
    print(user)

