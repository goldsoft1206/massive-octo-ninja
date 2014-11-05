from django.shortcuts import render
from django.views.generic import FormView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.forms import ProfileForm, UploadForm
from accounts.forms import UploadedFile


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

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['pictures'] = UploadedFile.objects.filter(user=self.request.user, file_type='P')
        return context


def upload_file(request):
    print request.POST, request.FILES
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/profile')
    #return render(request, 'upload.html', {'form': form}
    return HttpResponseRedirect('/profile')


class RemoveUploadView(DeleteView):
    model = UploadedFile
    success_url = '/profile'
    template_name = 'confirm_delete.html'

