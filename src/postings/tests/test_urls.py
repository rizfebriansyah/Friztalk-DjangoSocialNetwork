from django.test import SimpleTestCase
from django.urls import reverse, resolve
from postings.views import post_remark_create_and_list_view, love_dislike_post, UserPostUpdateView, UserPostDeleteView

class TestUrls(SimpleTestCase):

    def test_main_post_url_is_resolved(self):
        url = reverse('main-post-view')
        self.assertEquals(resolve(url).func, post_remark_create_and_list_view)

    def test_love_post_url_is_resolved(self):
        url = reverse('love-post-view')
        self.assertEquals(resolve(url).func, love_dislike_post)

    def test_update_url_is_resolved(self):
        url = reverse('post-update')
        self.assertEquals(resolve(url).func.view_class, UserPostUpdateView)

    def test_delete_url_is_resolved(self):
        url = reverse('post-delete')
        self.assertEquals(resolve(url).func.view_class, UserPostDeleteView)