from django import template
from django.contrib.auth import get_user_model
# from django.utils.html import escape
# from django.utils.safestring import mark_safe
from django.utils.html import format_html

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



