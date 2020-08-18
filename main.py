import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymysql import install_as_MySQLdb
from faker import Faker

from models import BaseModel
from models import Image
from models import Post
from models import ImagePost
from models import User


install_as_MySQLdb()
DATABASE_URL = 'mysql://root@localhost:3306/db'

engine = create_engine(DATABASE_URL)
BaseModel.metadata.drop_all(bind=engine)
BaseModel.metadata.create_all(bind=engine)
SessionMaker = sessionmaker(bind=engine)


def fill_data():
    fake = Faker()
    db = SessionMaker()
    users = [
        User(
            login=fake.email(),
            posts=[
                Post(
                    title=fake.sentence(),
                    body=fake.text(),
                ) for _ in range(random.randint(3,7))
            ]
        ) for _ in range(random.randint(5, 15))
    ]
    images = [
        Image(url=fake.image_url())
        for _ in range(random.randint(50,100))
    ]
    db.add_all(users)
    db.add_all(images)
    db.commit()

    post_ids = [p[0] for p in db.query(Post.id).all()]
    image_ids = [i[0] for i in db.query(Image.id).all()]
    secondary_records = []
    for post_id in post_ids:
        chosen_image_ids = random.sample(image_ids, k=random.randint(1, 10))
        for image_id in chosen_image_ids:
            secondary_records.append(
                ImagePost(post_id=post_id, image_id=image_id)
            )
    db.add_all(secondary_records)
    db.commit()

if __name__ == '__main__':
    fill_data()
