from django.db import models
from userprofiles.models import Profile
from django.core.validators import FileExtensionValidator

# Create your models here.
class UserPost(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='postings', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    loved = models.ManyToManyField(Profile, blank=True, related_name='loves')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.content[:20])

    def num_loves(self):
        return self.loved.all().count()
    
    def num_remarks(self):
        return self.remark_set.all().count()

    class Meta:
        ordering = ('-created',)

class Remark(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

LOVE_CHOICES = (
    ('Love', 'Love'),
    ('Dislike', 'Dislike'),
)

class Love(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    value = models.CharField(choices=LOVE_CHOICES, max_length=9)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
