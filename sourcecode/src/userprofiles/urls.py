from django.urls import path
from .views import (
    my_profilepage_view, 
    view_received_invites,
    user_profiles_list_view,
    invite_user_profiles_list_view,
    UserProfileListView,
    send_friend_invitation,
    erase_from_friends,
    deny_invitation,
    approve_invitation,
    UserProfileDetailView,
    search_friends,
)
app_name = 'userprofiles'

urlpatterns = [
    path('', UserProfileListView.as_view(), name='all-user-profiles-view'),
    path('myprofilepage/', my_profilepage_view, name='my-profilepage-view'),
    path('my-friend-invites/', view_received_invites, name='my-friend-invites-view'),
    path('invite-list-profiles/', invite_user_profiles_list_view, name='invite-user-profiles-view'),
    path('invite-send/', send_friend_invitation, name='invite-send'),
    path('erase-friend/', erase_from_friends, name='erase-friend'),
    path('my-friend-invites/approve/', approve_invitation, name='approve-invite'),
    path('my-friend-invites/deny/', deny_invitation, name='deny-invite'),
    path('<slug>/', UserProfileDetailView.as_view(), name='user-profile-detail-view'),
    path('search-friends/', search_friends, name='search-friends'),


]

