from .models import Profile

def add_user_profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        return {'profile': profile}
    return {}