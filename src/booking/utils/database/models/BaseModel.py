from peewee import *
from ..DatabaseProvider import get_db


class BaseModel(Model):
    """
    Base mysql model class.
    """
    class Meta:
        database = get_db()
