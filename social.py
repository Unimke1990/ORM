from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import uuid


Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    userID = Column("userID", String, primary_key=True, default=generate_uuid)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    profileName = Column("profileName", String)
    email = Column("email", String)

    def __init__(self, firstName, lastName, profileName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email


    def create_user(session, firstName, lastName, profileName, email):
        existing_user = session.query(User).filter_by(firstName=firstName, lastName=lastName, profileName=profileName, email=email).first()
        if existing_user:
            print(f"{firstName} {lastName} already exist")
            return existing_user
        else:
            new_user = User(firstName=firstName, lastName=lastName, profileName=profileName, email=email)
            session.add(new_user)
            session.commit()
            print("new user added successfully!")
            return new_user

class Posts(Base):
    __tablename__ = "newPosts"

    postID = Column("postID", String, primary_key=True, default=generate_uuid)
    userID = Column("userID", String, ForeignKey("users.userID"))
    postContent = Column("postContent", String)

    def __init__(self, userID, postContent):
        self.userID = userID
        self.postContent = postContent

    def add_post(userID, postContent, session):
        new_post = Posts(userID, postContent)
        session.add(new_post)
        session.commit()
        return new_post


engine = create_engine("sqlite:///socialDB.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



user1 = User.create_user(firstName="given", lastName="agim", profileName="agim_g", email="agimg@gmail.com", session=session)
user2 = User.create_user(firstName="chris", lastName="obi", profileName="chris02", email="chris02@gmail.com", session=session)
session.add_all([user1, user2])
session.commit()

user2 = Posts.add_post(userID=user2.userID, postContent="hello, this is my second post", session=session)
user2.postContent = "Hello, this is my first post"
session.add(user2)
session.commit()






# creating a post
# user_id = "2b337d10-ebc7-45b0-ae68-4768a9b3be2b"
# post_content = "This is my second post"

# agim_user = Posts(user_id, post_content)
# session.add(agim_user)
# session.commit()





