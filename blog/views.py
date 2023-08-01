from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import PostForm , CommentForm

from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

# Create your views here.
def posts_list(request):
    data = Post.objects.all()
    return render(request , "post_list.html" , {'posts': data})
# post_list --> templte  
 # post_list --> context


class PostList(ListView):
    model = Post


def post_detail(request , post_id):
    data = Post.objects.get(id = post_id)
    post_comments = Comment.objects.filter(post=data)
    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.user= request.user
            myform.post = data
            myform.save()
            
    else:
            form = CommentForm()
        
    
    return render(request , "blog/post_detail.html" , {"post":data , 'form':form , 'comments':post_comments})

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





