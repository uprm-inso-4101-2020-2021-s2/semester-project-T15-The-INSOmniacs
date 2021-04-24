from config.config import connect


class CoursesDAO:

    def __init__(self):
        connect(self)