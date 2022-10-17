from django.shortcuts import render, redirect
from userprofiles.models import Profile
from .models import UserPost, Love
from .forms import UserPostModelForm, RemarkModelForm
from django.views.generic import UpdateView, DeleteView
#from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def post_remark_create_and_list_view(request):
    qs = UserPost.objects.all()
    profile = Profile.objects.get(user=request.user)
 
    p_form = UserPostModelForm()
    q_form = RemarkModelForm()
    post_added = False
    
    profile = Profile.objects.get(user=request.user)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        p_form = UserPostModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = UserPostModelForm()
            post_added = True

    if 'submit_q_form' in request.POST:
        q_form = RemarkModelForm(request.POST)
        if q_form.is_valid():
            instance = q_form.save(commit=False)
            instance.user = profile
            instance.post = UserPost.objects.get(id=request.POST.get('post_id'))
            instance.save()
            q_form = RemarkModelForm()     
    

    context = {
        'qs': qs,
        'profile': profile,
        'p_form': p_form,
        'q_form': q_form,
        'post_added': post_added,
    }

    return render(request, 'posts/main.html', context)

@login_required
def love_dislike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = UserPost.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.loved.all():
            post_obj.loved.remove(profile)
        else:
            post_obj.loved.add(profile)

        love, created = Love.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if love.value=='Love':
                love.value='Dislike'
            else:
                love.value='Love'
        else:
            love.value='Love'

            post_obj.save()
            love.save()

        #data = {
            #'value': love.value,
            #'loves': post_obj.loved.all().count()
        #}

        #return JsonResponse(data, safe=False)

    return redirect('postings:main-post-view')

class UserPostDeleteView(LoginRequiredMixin, DeleteView):
    model = UserPost
    template_name ='posts/confirm_erase.html'
    success_url = reverse_lazy('postings:main-post-view')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = UserPost.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, 'You MUST be the author of this POST to ERASE')
        return obj

class UserPostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserPostModelForm
    model = UserPost
    template_name = 'posts/update.html'
    success_url = reverse_lazy('postings:main-post-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You MUST be the author of this POST to UPDATE")
            return super().form_invalid(form)