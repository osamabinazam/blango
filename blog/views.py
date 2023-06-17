from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
# Create your views here.

# Home Page
def index (request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  print(posts)
  context = {"posts" : posts}
  return render(request, "blog/index.html", context=context)


# Post Detail

def post_detail (request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.user.is_active:
    if request.method =='POST':
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object=post
        comment.creator=request.user
        comment.save()
        return redirect(request.path_info)
    else :
      comment_form =  CommentForm()
  else:
    comment_form = None
  
  
  context = {'post': post, 'comment_form': comment_form}
  return render(request, 'blog/post-detail.html', context=context )
 