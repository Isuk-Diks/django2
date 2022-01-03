from django.shortcuts import render
from .models import Profile


def my_profile(request):
	user = request.user
	profile = Profile.objects.filter(user=user).first()
	if not profile:
		profile = Profile.objects.create(user=user)
	if request.method == "POST":
		profile.position = request.POST['position']
		profile.website = request.POST['website']
		profile.description = request.POST['description']
		profile.mention = request.POST['mention']
		profile.user.first_name = request.POST['first_name']
		profile.user.last_name = request.POST['last_name']
		profile.save()
		profile.user.save()
	return render(request, "client_profile/my_profile.html", {"profile":profile})

def profile(request, username):
	user = request.user
	profile = Profile.objects.filter(user=user).first()
	return render(request, "client_profile/profile.html", {"profile":profile})