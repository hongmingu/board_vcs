from django.db import models
from django.utils import timezone
# Create your models here.



class PostAll(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "All// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)

class PostForMonth(models.Model):
    text = models.TextField(max_length=2020)
    title = models.TextField(max_length=30)


    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "For month// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.title)

class PostForMonthComment(models.Model):
    text = models.TextField(max_length=2020)
    post = models.ForeignKey(PostForMonth)


    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ForMonthComment// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.post.title)


class PostForHour(models.Model):
    text = models.TextField(max_length=2020)
    title = models.TextField(max_length=30)


    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "For hour// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.title)

class PostForHourComment(models.Model):
    text = models.TextField(max_length=2020)
    post = models.ForeignKey(PostForHour)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ForHourComment// PK : %s// created : %s // %s // " % (self.pk, self.createdAt, self.post.title)


class PostArabic(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Arabic// PK : %s// created : %s // %s // " %(self.pk, self.createdAt,  self.text)


class PostBengali(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Bengali// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostChinese(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Chinese// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostEnglish(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "English// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostFrench(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "French// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostGerman(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "German// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostHindi(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Hindi// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostJapanese(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Japanese// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostJavanese(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Javanese// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostKorean(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Korean// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostLahnda(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Lahnda// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostMalay(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Malay// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostPortuguese(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Portuguese// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostRussian(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Russian// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostSpanish(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Spanish// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)


class PostTelugu(models.Model):
    text = models.TextField(max_length=110)

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Telugu// PK : %s// created : %s // %s // " % (self.pk, self.createdAt,  self.text)

