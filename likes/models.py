from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.



class LikedItem(models.Model):
    # which user liked which item
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    #item kiss table say belong krta hay us table ki type 
    content_type = models.ForeignKey(ContentType , on_delete= models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
