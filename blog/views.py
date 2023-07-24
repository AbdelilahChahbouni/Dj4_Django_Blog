from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

# Create your views here.
def posts_list(request):
    data = Post.objects.all()
    return render(request , "post_list.html" , {'posts': data})

# views based class :
class PostList(ListView):
 # post_list --> templte  
 # post_list --> context
    model = Post


def post_detail(request , post_id):
    data = Post.objects.get(id = post_id)
    return render(request , "post_detail.html" , {"detail":data})

class PostDetail(DetailView):
    model = Post

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author = request.user
            my_form.save()
            return redirect("/blog")
    else:
        form = PostForm()
    form = PostForm()
    return render(request , 'create_post.html' , {"form": form})

class CreatePost(CreateView):
    model = Post
    fields = ['title' , 'content' , 'create_date' , 'draft' , 'tags' , 'image']
    success_url = '/blog'


def edit_post(request , post_id):
      data = Post.objects.get(id = post_id) 
      if request.method == "POST":
        form = PostForm(request.POST , request.FILES , instance=data)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author = request.user
            my_form.save()
            return redirect("/blog")
      else:
        form = PostForm(instance=data)
    
      return render(request , 'create_post.html' , {"form": form})

class EditePost(UpdateView):
    model = Post
    fields = ['title' , 'content' , 'create_date' , 'draft' , 'tags' , 'image']
    success_url = '/blog'
    template_name = 'blog/edite_post.html'
    

class DeletePost(DeleteView):
    model = Post
    success_url = '/blog'


def delete_post(request , post_id):
    data = Post.objects.get(id = post_id)
    data.delete()
    return redirect("/blog")





