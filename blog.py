from sqlalchemy import create_engine, Column, String, CHAR, ForeignKey, Integer, and_, or_
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    userID = Column("userID", String, primary_key=True, default=generate_uuid)
    userName = Column("userName", String)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    posts = relationship("Posts", back_populates="user")

    def __init__(self, userName, firstName, lastName):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName

    @staticmethod   
    def createUser(session, userName, firstName, lastName):
        existingUser = session.query(User).filter_by(userName=userName, firstName=firstName, lastName=lastName).first()
        if existingUser:
            print("user already exist")
            return existingUser
        else:
            newUser = User(userName=userName, firstName=firstName, lastName=lastName)
            session.add(newUser)
            session.commit()
            print("new user succesfully added")
            return newUser


class Posts(Base):
    __tablename__ = "posts"
    postID = Column("postID", String, primary_key=True, default=generate_uuid)
    userID = Column("userID", String, ForeignKey("users.userID"))
    postContent = Column("postContent", String)
    user = relationship("User", back_populates="posts")

    def __init__(self, userID, postContent):
        self.userID = userID
        self.postContent = postContent

    @staticmethod
    def addPost(session, userID, postContent):
        newPost = Posts(userID=userID, postContent=postContent)
        session.add(newPost)
        session.commit()
        return newPost


engine = create_engine("sqlite:///blogDB.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# adding users
user1 = User.createUser(session=session, userName="Beatrice_J", firstName="Beatrice", lastName="John")
user2 = User.createUser(session=session, userName="PuoloG", firstName="Paul", lastName="Jimmy")
user3 = User.createUser(session=session, userName="Angel", firstName="Simmy", lastName="Dal")
user4 = User.createUser(session=session, userName="Angel", firstName="Agba", lastName="Dal")
user5 = User.createUser(session=session, userName="PuoloG", firstName="Clop", lastName="Danny")

# adding posts
user1 = Posts.addPost(session=session, userID=user1.userID, postContent="hello, this is my third post")
user1 = Posts.addPost(session=session, userID=user1.userID, postContent="hello, this is my fourth post")
user2 = Posts.addPost(session=session, userID=user2.userID, postContent="hello, this is my third post")
user2 = Posts.addPost(session=session, userID=user2.userID, postContent="hello, this is my fourth post")

# querying the data
user_query = session.query(User).filter_by(firstName="Paul").first()
for allPosts in user_query.posts:
    print(allPosts.postContent)

post_query = session.query(Posts).filter_by(postContent="hello, this is my first post").all()
for all_post in post_query:
    print(all_post.user.userID)

checks = session.query(User).filter(or_(User.userName=="Angel", User.firstName=="Agba")).all()
for check in checks:
    print(f"{check.userName}, {check.firstName}, {check.userID}")

checks = session.query(User).filter(and_(User.userName=="Angel", User.lastName=="Simmy")).all()
for check in checks:
    print(f"{check.userName}, {check.firstName}, {check.userID}")

checkAllPost = session.query(User).filter_by(userName="Beatrice_J").first()
if checkAllPost:
    print(f"{checkAllPost.firstName}, {checkAllPost.userID}")

    for post in checkAllPost.posts:
        print(f"{post.postContent}")
else:
    print("user not found")