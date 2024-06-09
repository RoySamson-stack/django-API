from tastypie.resources import ModelResource
from api.models import Note

class NoteResources(ModelResource):
    class Meta:
        queseryset = Note.object.all()
        resource_name = 'note'