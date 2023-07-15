from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def posts_list(request):
    data = Post.objects.all()
    return render(request , "post_list.html" , {'posts': data})

def post_detail(request , post_id):
    data = Post.objects.get(id = post_id)
    return render(request , "post_detail.html" , {"detail":data})



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


def edit_post(request , post_id):
    pass

def delete_post(request , post_id):
    pass



