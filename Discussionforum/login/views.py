from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import discussion
from .models import comment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import commentForm
from django.shortcuts import redirect



def index(request):
    posts = discussion.objects.order_by('created_date_discussion')
    comments=comment.objects.order_by('created_date_discussion')
    return render(request, 'login/post_list.html', {'posts': posts,'comments':comments})

def post_detail(request, pk):
    post = get_object_or_404(discussion, pk=pk)
    form = commentForm(request.POST)
    if request.method == "POST":
        #form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion_id=post
            #discussion.usser_account_id=request.user
            comment.content = form['content'].value()
            comment.created_date_discussion = timezone.now()
            comment.save()
            return redirect('index')
        else:
            form = commentForm()
    return render(request, 'login/post_detail.html', {'post': post, 'form':form})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            #discussion.usser_account_id=request.user
            discussion.subject = form['subject'].value()
            discussion.created_date_discussion = timezone.now()
            discussion.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'login/post_edit.html', {'form': form})