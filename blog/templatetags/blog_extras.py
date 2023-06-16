from django import template
from django.contrib.auth import get_user_model
# from django.utils.html import escape
# from django.utils.safestring import mark_safe
from django.utils.html import format_html
from blog.models import Post

user_model = get_user_model()
register = template.Library()

@register.filter(name="author_details")           # Registering the filter to template Library
def author_details(author, user=None):
  if not isinstance(author, user_model):
    # returning empty string as safe exit
    return ""
  if author == user:
    return format_html('<strong>me</strong>')
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"
  
  if author.email:
    # email = escape (author.email)
    # prefix = f'<a href="mailto:{email}">'
    prefix = format_html ('<a href="mailto:{}">', author.email)
    suffix = format_html("</a>")
  else :
    prefix=""
    suffix=""
  # return mark_safe(f"{prefix}{name}{suffix}")
  return format_html('{}{}{}', prefix, name, suffix)



# Define Custom Row Template tag
@register.simple_tag
def row (extra_classes=""):
  return format_html('<div class= "row {}" >', extra_classes)
@register.simple_tag
def endrow():
  return format_html('</div>')


# Define Custom Col Template tag
@register.simple_tag
def col(extra_classes=""):
  return format_html(' <div class= "{}" >', extra_classes)
@ register.simple_tag
def endcol():
  return format_html("</div>")


# Fetch Recent post
@register.inclusion_tag('blog/post-list.html')
def recent_posts(post):
  posts = Post.objects.exclude(pk = post.pk)[:5]
  print(posts)
  context = {
    "title": "Recent posts",
    "posts":posts
    
  }
  return context
  

# Just for practice purpose

# Define Custom template tag for author detail
# @register.simple_tag(takes_context=True)
# def author_details_tag(context):
#   request = context["request"]
#   current_user =  request.user
#   post = context["post"]
#   author = post.author
#   if author == current_user:
#     return format_html("<strong>me</strong>")
#   if author.first_name and author.last_name:
#     name = f'{author.first_name} { author.last_name}'
#   else : 
#     name = f'{author.username}'
#   if author.email:
#     prefix = format_html('<a href= "mailto: {}">', author.email)
#     suffix = format_html('</a>')
#   else:
#     prefix =""
#     suffix = ""
  
#   return format_html('{} {} {}', prefix, name, suffix)
