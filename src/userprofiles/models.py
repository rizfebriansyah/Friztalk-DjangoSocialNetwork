from django.db import models
from django.contrib.auth.models import User
from .utils import generate_random_character
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

# Create your models here.
class ProfileManager(models.Manager):

    def attain_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Connection.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("############################")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("############################")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("############################")      
        return available
        

    def attain_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

class Profile(models.Model):
    f_name = models.CharField(max_length=250, blank=True)
    l_name = models.CharField(max_length=250, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(default="bio is empty", max_length=350)
    email = models.EmailField(max_length=200, blank=True)
    residence = models.CharField(max_length=200, blank=True)
    profile_picture = models.ImageField(default='profilepic.png', upload_to='profilepics/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    
    def attain_absolute_url(self):
        return reverse("userprofiles:user-profile-detail-view", kwargs={"slug": self.slug})

    def attain_friends(self):
        return self.friends.all()

    def attain_friends_number(self):
        return self.friends.all().count()

    def attain_posts_number(self):
        return self.posts.all().count()

    def attain_all_authors_posts(self):
        return self.posts.all()

    def attain_loves_given_number(self):
        loves = self.love_set.all()
        total_loved = 0
        for item in loves:
            if item.value=='Love':
                total_loved += 1
        return total_loved

    def attain_loves_received_number(self):
        posts = self.posts.all()
        total_loved = 0
        for item in posts:
            total_loved += item.loved.all().count()
        return total_loved

    __initial_f_name = None
    __initial_l_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_f_name = self.f_name
        self.__initial_l_name = self.l_name

    def save(self, *args, **kwargs):
        excheck = False
        to_slug = self.slug
        if self.f_name != self.__initial_f_name or self.l_name != self.__initial_l_name or self.slug=="":
            if self.f_name  and self.l_name:
                to_slug = slugify(str(self.f_name) + " " + str(self.l_name))
                excheck = Profile.objects.filter(slug=to_slug).exists()
                while excheck:
                        to_slug = slugify(to_slug + " " + str(generate_random_character()))
                        excheck = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class ConnectionManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Connection.objects.filter(receiver=receiver, status='send')
        return qs


class Connection(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ConnectionManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
