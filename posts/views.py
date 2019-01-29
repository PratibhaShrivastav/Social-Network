from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


from posts.models import Post,Comment
from django.forms import forms
from django.contrib.auth import get_user_model

"""returns the active User model"""
User=get_user_model()


"""This view is used to get the list of all the posts""" 
class PostList(SelectRelatedMixin,ListView):
    model=Post

    """used to effectively extract values of Foreign Key fields"""
    select_related=('user','group')

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


"""This view is used to get user specific posts"""
class UserPosts(SelectRelatedMixin,ListView):
    model=Post
    template_name='posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user=Post.objects.filter(user__username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            return Http404
        else:
            return self.post_user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.kwargs.get('username')
        return context


"""This view is used to get the complete details of a post"""
class PostDetail(SelectRelatedMixin,DetailView):
    model=Post
    select_related=('user','group')
    context_object_name='post'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User
        return context
                                                  

"""This view is used for creation of a new post"""
class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    model=Post
    fields=('group','message')

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)


"""This view is used for updating or editing an existing post"""
class UpdatePost(LoginRequiredMixin,UpdateView):
    model=Post
    fields=('group','message')


"""This view is used for the deletion of a post"""
class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('posts:all')
    select_related=('user','group')

    def get_queryset(self):
        queryset= super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post deleted successfully')
        return super().delete(*args,**kwargs)


"""This view is used for comment adding"""
class AddComment(LoginRequiredMixin,CreateView):
    model=Comment
    fields=('text',)
    #;success_url=reverse_lazy('posts:all',kwargs={'username'})

    def form_valid(self, form):
        post=get_object_or_404(Post,pk=self.kwargs['pk'])
        self.object=form.save(commit=False)
        self.object.author=self.request.user
        self.object.post=post
        return super().form_valid(form)

    def get_success_url(self):
        post=get_object_or_404(Post,pk=self.kwargs['pk'])
        username = post.user.username
        pk = post.pk
        return reverse_lazy('posts:single',kwargs={'username':username,'pk':pk})


"""This view is for updating elements"""
class DeleteComment(LoginRequiredMixin,DeleteView):
    model=Comment
    
    def get_success_url(self):
        post=get_object_or_404(Post,pk=self.kwargs['postpk'])
        username = post.user.username
        pk = post.pk
        return reverse_lazy('posts:single',kwargs={'username':username,'pk':pk})