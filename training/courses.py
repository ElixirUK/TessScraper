__author__ = 'milo'

import uuid
import json

# A general class of which tutorials, face-to-face courses &c. are a subclass.
# All of these will need a name, id, url and so on, so it make sense to subclass
# the other types.
# 0: Name of tutorial
# 1: URL
# 2: Name of tutorial  it follows on from [UUID]
# 3: links to resources / tools used
# 4: DOI
# 5: Keywords
class TuitionUnit:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = None
        self.url = None
        self.parent_id = None # id of preceeding tutorial/class &c.
        self.resources = []
        self.doi = None
        self.keywords = []
        self.difficulty = None
        self.owning_org = None # CKAN owning organisation
        self.audience = []

    # CKAN expects some JSON to be sent when creating new objects.
    def dump(self):
        data = {'id': str(self.id),
                'name': self.name,
                'url': self.url,
                'parent_id': self.parent_id,
                'doi': self.doi,
                'keywords': self.keywords,
                'difficulty': self.difficulty,
                'owning_org': self.owning_org
                }
        return data


# 6: Name of author
# 7: Date created
# 8: Date of last update
# 9: Difficulty rating out of 5 stars
class Tutorial(TuitionUnit):
    def __init__(self):
        TuitionUnit.__init__(self)
        self.author = None
        self.created = None
        self.last_update = None

    def dump(self):
        data = TuitionUnit.dump(self)
        data['author'] = self.author
        data['created'] = self.created
        data['last_update'] = self.last_update
        return data


# 6: Organisers
# 7: Date(s) of event
# 8: Difficulty rating out of 5 stars
class FaceToFaceCourse(TuitionUnit):
    def __init__(self):
        TuitionUnit.__init__(self)
        self.organisers = []
        self.dates = [] # start 0, end 1 ?

    def dump(self):
        data = TuitionUnit.dump(self)
        data['organisers'] = self.organisers
        data['dates'] = self.dates
        return data