from unittest import TestCase


from django.test import TestCase
from userprofiles.models import ProfileManager, Profile, ConnectionManager, Connection

class TestModels(TestCase):
    
    def setUp(self):
        self.profile1 = Profile.objects.create(
            name='Profile 1',
            biography='happy 1'
        )