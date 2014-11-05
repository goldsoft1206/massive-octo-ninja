from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.forms import ProfileForm


class ProfileView(FormView):
    """
    ProfileView
    """
    form_class = ProfileForm
    template_name = "profile.html"
    success_url = '/profile'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        return {'title':self.request.user.profile.title}

    def form_valid(self, form):
        self.request.user.profile.title = form.cleaned_data['title']
        self.request.user.profile.save()
        return super(ProfileView, self).form_valid(form)