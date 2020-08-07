from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, help_text="example: languages, projects, CV..")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # post numbering : first post -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def is_content_more(self):
        post_length = 300
        return len(self.content) > post_length

    def get_content_under(self):
        post_length = 300
        return self.content[:post_length]