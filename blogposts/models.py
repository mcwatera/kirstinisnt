from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager


#class ImageAlbum(models.Model):
#    def default(self):
#        return self.images.filter(default=True).first()

class Blogpost(models.Model):
    blog_post_title = models.CharField(max_length=60, help_text='Title')
    blog_post_content = HTMLField()
    blog_post_date = models.DateField()
    #blog_post_pics = models.OneToOneField(ImageAlbum, null=True, blank=True, related_name='model', on_delete=models.CASCADE)
    blog_post_tags = TaggableManager()
    
    def __str__(self):
        return self.blog_post_title

class BlogpostComment(models.Model):
    comment_contents = models.TextField()
    comment_post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    comment_date = models.DateField
    

#class Image(models.Model):
#    name = models.CharField(max_length=255)
#    image = models.ImageField(upload_to="images/")
#    default = models.BooleanField(default=False)
#    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

            
    