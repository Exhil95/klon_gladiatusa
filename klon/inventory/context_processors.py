from user_profile.models import UserProfile

def player_banner_context(request):
    if request.user.is_authenticated:
        try:
            player = UserProfile.objects.get(user=request.user)
            return {'player': player}
        except UserProfile.DoesNotExist:
            return {}
    return {}