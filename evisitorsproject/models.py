from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# Create your models here.

class Image(models.Model):
    '''
     This is a Image model to represent Image table whithin the database
    '''
    image = models.ImageField(upload_to ="photos/",null = True)
    user = models.ForeignKey(User,null = True)
    image_name = models.CharField(max_length =30, null= True)
    votes = models.IntegerField(default = 0)
    image_caption = models.TextField( null = True)
    pub_date = models.DateTimeField(auto_now_add = True, null =True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.pic_name

    def delete_image(self):
        self.delete()
    def save_image(self):
        self.save()
    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls,id):
        share_images = Image.objects.filter(user_id=id)
        return share_images

    @classmethod
    def get_images_by_id(cls,id):
        retrieved_image = Image.objects.get(id = id)
        return retrieved_image
    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.image_name

    def save_profile(self):
        self.save()
# class Idscan(models.Model):
#     scanId=model.IntegerField(default)

