from django.forms import ModelForm
from accounts.models import Profile, UploadedFile


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['title']


class UploadForm(ModelForm):
	class Meta:
		model = UploadedFile
		exclude = ['upload_dt']
