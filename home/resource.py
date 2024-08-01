from import_export import resources 
from .models import Dr

class DrResource(resources.ModelResource):
     class Meta:
         model = Dr