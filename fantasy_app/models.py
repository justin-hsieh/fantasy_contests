from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)

DB = SQLAlchemy()

