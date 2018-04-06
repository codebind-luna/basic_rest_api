from falcon_autocrud.resource import CollectionResource, SingleResource
from models import Note

class NoteCollectionResource(CollectionResource):
    model = Note

class NoteResource(SingleResource):
    model = Note
