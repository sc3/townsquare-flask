
from . import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

class TimeEntry(db.Model):
    """
    A time entry is used to record when a user needs to log
    in some amount of time.

    The time entry has a beginning and a ending.

    The "activity" taxonomy to categorize what the user is logging
    time for.  For example, having a activity with a value of
    "Open Build" means that the user was participating in
    "Open Build" in the time specified.

    """

    __tablename__ = 'time_entries'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    # activity_id = Column(Integer, ForeignKey('activities.id'))

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    def __init__(self):
        self.start_time = datetime.utcnow()
