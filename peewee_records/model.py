from peewee import *
# from peewee_records.database_config import database_path

db = SqliteDatabase('recordsPeewee.sqlite')


class Record(Model):

    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db
        # indexes = (
        #     (('name','country'),True ),
        # )



db.connect()
db.create_tables([Record])