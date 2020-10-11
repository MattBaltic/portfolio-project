from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    blog_content = models.TextField()
    image2 = models.ImageField(upload_to = 'images/')
