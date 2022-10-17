from unittest import TestCase


from django.test import TestCase
from postings.models import UserPost, Love, Remark

class TestModels(TestCase):
    
    def setUp(self):
        self.project1 = UserPost.objects.create(
            content='Project 1',

        )