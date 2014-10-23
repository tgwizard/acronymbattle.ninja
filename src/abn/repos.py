from slugify import slugify


class Acronym(object):
    def __init__(self, acronym, answer):
        self.acronym = acronym
        self.answer = answer


class Competition(object):
    def __init__(self, name, acronyms):
        self.name = name
        self.acronyms = acronyms

    @property
    def slug(self):
        return slugify(self.name)


class CompetitionRepo(object):
    _competitions = [
        Competition('Computer Science', [
            Acronym('DFS', 'Depth-first search'),
            Acronym('BFS', 'Breadth-first search'),
            Acronym('FSM', 'Finite state machine'),
            Acronym('DFA', 'Deterministic finite automaton'),
        ]),
        Competition('Computer Networks', [
            Acronym('DNS', 'Domain Name System'),
            Acronym('TCP', 'Transport Control Protocol'),
            Acronym('UDP', 'User Datagram Protocol'),
            Acronym('IP', 'Internet Protocol'),
        ]),
        Competition('Recursive Acronyms', [
            Acronym('GNU', "GNU's not Unix!"),
            Acronym('PHP', 'PHP: Hypertext Preprocessor'),
        ]),
    ]

    @classmethod
    def list(cls):
        return cls._competitions

    @classmethod
    def get(cls, slug):
        for competition in cls._competitions:
            if competition.slug == slug:
                return competition
