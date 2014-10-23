from slugify import slugify

class Competition(object):
    def __init__(self, name):
        self.name = name

    @property
    def slug(self):
        return slugify(self.name)


class CompetitionRepo(object):
    _competitions = [
        Competition('Computer Science'),
        Competition('Computer Networks'),
        Competition('Medicine'),
        Competition('Recursive Acronyms'),
    ]

    @classmethod
    def get_competitions(cls):
        return cls._competitions