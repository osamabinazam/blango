from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post
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
  context = {'post': post}
  return render(request, 'blog/post-detail.html', context=context )
 