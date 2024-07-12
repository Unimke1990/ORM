from main import User, engine
from sqlalchemy.orm import sessionmaker

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# create new users or check if user already exist
def create_users(name, age):
    existing_users = session.query(User).filter_by(name=name, age=age).first()
    if existing_users:
        return existing_users
    else:
        new_user = User(name=name, age=age)
        session.add(new_user)
        session.commit()
        return new_user


# Create User instances
user1 = create_users(name="agim given", age=34)
user2 = create_users(name="peace jane", age=26)
user3 = create_users(name="john kafor", age=31)
user4 = create_users(name="jane sip", age=26)
user5 = create_users(name="mma asaka", age=26)

# Add all User instances to the session
session.add_all([user1, user2, user3, user4, user5])
user = session.query(User).filter_by(id=6).one_or_none()


# changing or updating records. changes must be commited to take effect in the db
# user.name= "jenny brew"
# session.commit()
print(user.name)

# deleting records
session.delete(user)
session.commit()
# Commit the transaction
# session.commit()

# Query the database for all User instances
# all_users = session.query(User).all()
# print(all_users)

# new = session.query(User).filter_by(id=2).all()

# one_none means return only one of. it'll return an error if there are multiple matches
# age26 = session.query(User).filter_by(age=26).one_or_none()
# age26 = session.query(User).filter_by(age=26).all()
# # user_0 = all_users[0]
# print(all_users.name)
# print(user_0.id)
# print(user_0.name)
# print(user_0.age)

# print(age26)