from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userprofiles.views import UserProfileListView, my_profilepage_view, view_received_invites, invite_user_profiles_list_view, send_friend_invitation, erase_from_friends, approve_invitation, deny_invitation, UserProfileDetailView, search_friends

class TestUrls(SimpleTestCase):

    def test_profilepage_view_is_resolved(self):
        url = reverse('my-profilepage-view')
        self.assertEquals(resolve(url).func, my_profilepage_view)

    def test_view_received_invites_url_is_resolved(self):
        url = reverse('my-friend-invites-view')
        self.assertEquals(resolve(url).func, view_received_invites)

    def test_invite_user_profiles_url_is_resolved(self):
        url = reverse('my-friend-invites-view')
        self.assertEquals(resolve(url).func, invite_user_profiles_list_view)

    def test_send_friend_invitation_url_is_resolved(self):
        url = reverse('invite-send')
        self.assertEquals(resolve(url).func, send_friend_invitation)

    def test_erase_friends_url_is_resolved(self):
        url = reverse('erase-friend')
        self.assertEquals(resolve(url).func, erase_from_friends)

    def test_approve_invitation_url_is_resolved(self):
        url = reverse('approve-invite')
        self.assertEquals(resolve(url).func, approve_invitation)

    def test_deny_invitation_url_is_resolved(self):
        url = reverse('deny-invite')
        self.assertEquals(resolve(url).func, deny_invitation)

    def test_search_friends_url_is_resolved(self):
        url = reverse('search-friends')
        self.assertEquals(resolve(url).func, search_friends)

    def test_user_profile_list_is_resolved(self):
        url = reverse('all-user-profiles-view')
        self.assertEquals(resolve(url).func.view_class, UserProfileListView)

    def test_user_profile_detail_is_resolved(self):
        url = reverse('user-profile-detail-view')
        self.assertEquals(resolve(url).func.view_class, UserProfileDetailView)