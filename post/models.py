from django.db import models

# Create your models here.
class PostAll(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "All// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostForMonth(models.Model):
    text = models.TextField(max_length=2020)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ForMonth// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostArabic(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Arabic// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostBengali(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Bengali// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostChinese(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Chinese// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostEnglish(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "English// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostFrench(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "French// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostGerman(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "German// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostHindi(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Hindi// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostJapanese(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Japanese// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostJavanese(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Javanese// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostKorean(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Korean// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostLahnda(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Lahnda// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostMalay(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Malay// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostPortuguese(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Portuguese// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostRussian(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Russian// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostSpanish(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Spanish// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)

class PostTelugu(models.Model):
    text = models.TextField(max_length=60)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Telugu// %s // created : %s PK : %s" % (self.text, self.createdAt, self.pk)
