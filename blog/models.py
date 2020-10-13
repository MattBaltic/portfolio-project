from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    blog_content = models.TextField()
    image2 = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title #zamienia na stornie admin domyslne listy (blog object 1, blog object 2) na liste z title blogow

    def summary(self):
        return self.blog_content[:100]

    def publication_date_notime(self):
        return self.publication_date.strftime('%e %b %Y')
        # skraca czas tylko do daty, posortowane przy uzyciu srtftime (https://strftime.org/)
