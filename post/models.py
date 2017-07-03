from django.db import models

# Create your models here.
class PostAll(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)