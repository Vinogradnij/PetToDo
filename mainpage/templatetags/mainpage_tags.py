from django import template
from mainpage.models import *

register = template.Library()


@register.inclusion_tag('mainpage/template_extras/list_categories.html')
def show_categories():
    categories = Category.objects.order_by('name')
    return {'categories': categories}
