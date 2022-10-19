from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filname):
    return '/'.join(['images', str(instance.title), filname])


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True,
                              upload_to=upload_path)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    # last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True)
    post_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_post.all().count()

    def view_count(self):
        return self.postnowview_post.all().count()

    def like_count(self):
        return self.like_post.all().count()

    def likes_all(self):
        return self.like_post.all()

    def comments(self):
        return self.comment_post.all()


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment_post")
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="like_post")

    def __str__(self):
        return self.user.username


class PostNowView(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="postnowview_user")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="postnowview_post")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
