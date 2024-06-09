from tastypie.resources import ModelResource
from .models import Note

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        allowed_methods = ['get', 'post', 'put', 'delete']
