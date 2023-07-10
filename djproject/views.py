"""
To render html web pages
"""
import random
from django.http import HttpResponse

from django.template.loader import render_to_string

from articles.models import Article


def home_view(request, id=None, *args, **kwargs):
    """
    Take in a request (Django send request)
    return HTML as a response 
    (We pick to return the response)
    """
    name = "Artem" # hard coded
    number = random.randint(1, 2) # pseudo random


    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }

    # Django templates
    HTML_STRING =  render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)