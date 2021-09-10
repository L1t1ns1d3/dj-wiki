import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NewWikiForm
from . import util
from encyclopedia import forms


def index(request):
    if request.method == 'POST':
        query = request.POST['q']
        if util.get_entry(query):
            return HttpResponseRedirect(reverse('encyclopedia:wiki', args=[query]))
        final_entries = [entry for entry in util.list_entries() if query in entry]
        return render(request, 'encyclopedia/search.html', {
            'title': query,
            'entries': final_entries
        })


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    """ Get the content of that encyclopedia title """
    if not util.get_entry(title):
        return render(request, 'encyclopedia/404.html', {
            'not_found': 'The requested page is not found!'
        })
    return render(request, 'encyclopedia/entry.html', {
        'content': util.get_entry(title),
        'title': title
    })



def new_wiki(request):
    """ Create a new wiki entry """
    if request.method == 'POST':
        form = forms.NewWikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title):
                return render(request, 'encyclopedia/new_wiki.html', {
                    'error': 'The new encyclopedia entry is exist!'
                })
            util.save_entry(title, content)
        else:
            return render(request, 'encyclopedia/new_wiki.html', {
                'form': form
            })

    return render(request, 'encyclopedia/new_wiki.html', {
        'form': NewWikiForm()
    })


def edit_wiki(request, title):
    """ Edit an existing wiki entry """
    if request.method == 'POST':
        new_title = request.POST['edit_title']
        new_content = request.POST['edit_content']
        util.save_entry(new_title, new_content)
        return HttpResponseRedirect(reverse('encyclopedia:wiki', args=[new_title]))
    return render(request, 'encyclopedia/edit_wiki.html', {
        'title': title,
        'entry_data': util.get_entry(title)
    })


def random_wiki(request):
    """ Get a random wiki entry from the existing list and render it. """
    random_wiki_entry = random.choice(util.list_entries())
    return render(request, 'encyclopedia/random.html', {
        'random_wiki_entry': random_wiki_entry
    })
