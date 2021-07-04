from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from .forms import CommentForm
from blog.models import Post
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views import View
from django.shortcuts import get_object_or_404, render
import datetime
# from django.template import 

posts=[
    {
        "slug":"mountains0-article",
        "image":"mountains.jpeg",
        "author":"Vignesh K",
        "date": datetime.date(2021,6,5),
        "title":"Mountain Hiking",
        "excerpt":"There is nohing like the view in mountain that is why I am writing this article",
        "content":"""
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!
        """

    },
    {
        "slug":"mountains1-article",
        "image":"mountains.jpeg",
        "author":"Vignesh K",
        "date": datetime.date(2021,6,5),
        "title":"Mountain Hiking",
        "excerpt":"There is nohing like the view in mountain that is why I am writing this article",
        "content":"""
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!
        """

    },
    {
        "slug":"mountains2-article",
        "image":"mountains.jpeg",
        "author":"Vignesh K",
        "date": datetime.date(2021,6,5),
        "title":"Mountain Hiking",
        "excerpt":"There is nohing like the view in mountain that is why I am writing this article",
        "content":"""
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
            Animi facere praesentium quod alias expedita? 
            Debitis minus accusantium vitae optio excepturi nobis, 
            repellat iure fugit est unde aut quidem ab sunt!
        """

    },
    {
        "slug":"mountains3-article",
        "image":"mountains.jpeg",
        "author":"Vignesh K",
        "date": datetime.date(2021,6,5),
        "title":"Mountain Hiking",
        "excerpt":"There is nohing like the view in mountain that is why I am writing this article",
        "content":"""
            Lorem ipsum dolor sit, amet consectetur adipisicing elit.Animi facere praesentium quod alias expedita? Debitis minus accusantium vitae optio excepturi nobis, repellat iure fugit est unde aut quidem ab sunt!
            Lorem ipsum dolor sit, amet consectetur adipisicing elit.Animi facere praesentium quod alias expedita? Debitis minus accusantium vitae optio excepturi nobis, repellat iure fugit est unde aut quidem ab sunt!
            Lorem ipsum dolor sit, amet consectetur adipisicing elit.Animi facere praesentium quod alias expedita? Debitis minus accusantium vitae optio excepturi nobis, repellat iure fugit est unde aut quidem ab sunt!
            Lorem ipsum dolor sit, amet consectetur adipisicing elit.Animi facere praesentium quod alias expedita? Debitis minus accusantium vitae optio excepturi nobis, repellat iure fugit est unde aut quidem ab sunt!
        """

    }
]

# Create your views here.

def get_date(post):
    return post["date"]

def index(request):
    # sort_posts=sorted(posts,key=lambda post:post['date'])
    # latest_posts=sort_posts[-3:]
    # return render(request,"blog/index.html",{
    #     "posts":latest_posts
    # })
    posts=Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts":posts
    })

def all_posts(request):
    posts=Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{
        "all_posts":posts
    })

def individual_post(request,slug):
    # post=Post.objects.get(slug=slug)
    post=get_object_or_404(Post,slug=slug)

    # unique_post=None
    # for post in posts:
    #     if post['slug']==slug:
    #         unique_post=post
    return render(request,"blog/post-detail.html",{
        "post":post,
        "post_tags":post.tag.all()
    })

# class based views

class Index(ListView):
    template_name="blog/index.html"
    model=Post
    context_object_name="posts"
    def get_queryset(self):
        all_posts = super().get_queryset()
        return all_posts.order_by("-date")[:3]

class AllPosts(ListView):
    template_name="blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"
    def get_queryset(self):
        all_posts = super().get_queryset()
        return all_posts

class IndividualPost(DetailView):
    template_name="blog/post-detail.html"
    model=Post
    context_object_name="post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"]=self.object.tag.all()
        context["comment_form"]=CommentForm()
        return context

class SinglePost(View):

    def get(self,request,slug):
        post=get_object_or_404(Post,slug=slug)
        stored_posts=request.session.get("stored_posts")
        if stored_posts is not None:
            saved_for_later=post.id in stored_posts
        else:
            saved_for_later=False
        form=CommentForm()
        return render(request,"blog/post-detail.html",{
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":form,
            "comments":post.comments.all().order_by("-id"),
            "saved_for_later":saved_for_later
        })
    
    def post(self,request,slug):
        form=CommentForm(request.POST)
        post=get_object_or_404(Post,slug=slug)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))

        return render(request,"blog/post-detail.html",{
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":form,
            "comments":post.comments.all()
        })

class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        print(stored_posts)
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            context["posts"]=Post.objects.filter(id__in=stored_posts)
            context["has_posts"]=True
        return render(request,"blog/stored-posts.html",context)

    def post(self,request):
        post_id=int(request.POST["post_id"])
        post_slug=request.POST["post_slug"]
        stored_posts=request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts=[]
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"]=stored_posts
        return HttpResponseRedirect(reverse("post-detail-page",args=[post_slug]))