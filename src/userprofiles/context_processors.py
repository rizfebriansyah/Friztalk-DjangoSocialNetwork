from .models import Profile, Connection

def display_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.profile_picture
        return {'picture':pic}
    return {}

def number_invitations_received(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Connection.objects.invitations_received(profile_obj).count()
        return {'number_invites':qs_count}
    return {}