from kino import general
from model import session


session.add(general())
session.commit()