from peewee import *

db = SqliteDatabase('sprint_reporter.db')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class UserStory(BaseModel):
    title = CharField()
    story = CharField()
    criteria = CharField()
    value = IntegerField()
    time = FloatField()
    status = CharField()


    @classmethod
    def add_user_story(cls, dictionary):
        cls.create(**dictionary)


    @classmethod
    def list_all(cls):
        query = cls.select()
        return query