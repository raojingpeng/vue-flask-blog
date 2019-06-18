# -*- coding: utf-8 -*-
"""
    :author: raojingpeng
    :github: https://github.com/raojingpeng
    :email: withrjp@gmail.com
"""
from blog import db
from blog.models import Post
import random
from faker import Faker

fake = Faker()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(nb_words=3),
            summary=fake.text(30),
            markdown=fake.text(100),
            html=fake.text(100),
            timestamp=fake.date_time_this_year(),
            views=random.randint(0, 100),
            user_id=1
        )
        db.session.add(post)

    db.session.commit()
