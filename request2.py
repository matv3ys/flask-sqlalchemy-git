db_name = input()

global_init(db_name)
session = create_session()


for user in session.query(User).filter(User.address == 'module_1',
                                       User.speciality.notlike('%ingeneer%'),
                                       User.position.notlike('%ingeneer%')):
    print(user.id)