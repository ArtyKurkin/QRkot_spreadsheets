from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import AbstractBase


class Donation(AbstractBase):
    """ Donation model. """
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
