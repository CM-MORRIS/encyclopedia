from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    entry_info = util.get_entry(entry)

    if entry_info is None:
        entry_info = "Error page not found"
        entry = "Page not found"


    return render(request, "encyclopedia/entry.html", {
        "entry_info": entry_info,
        "title": entry
    })


def search(request):

    if (request.method == 'GET'):
        return HttpResponse("Please use search function")

    # else POST request
    else:
        search_query = request.POST['q']
        entry = util.get_entry(search_query)

        if entry is None:

            all_entries = util.list_entries()

            #matching_results = [s for s in all_entries if search_query in s]
            matching_results = filter(lambda x: search_query.capitalize() in x, all_entries)

            return render(request, "encyclopedia/search_results.html", {
                "matching_results": matching_results
            })

        # else show the valid entry
        return render(request, "encyclopedia/entry.html", {
            "entry_info": entry,
            "title": search_query
        })

def create_new_page(request):

    if (request.method == 'GET'):
        return render(request, "encyclopedia/create_new_page.html")

    else:
        new_page_title = request.POST['new_page_title']
        new_page_info = request.POST['new_page_info']

        # if not already exists Add
        if (new_page_title not in util.list_entries()):
            util.save_entry(new_page_title, new_page_info)
            return redirect('entry', entry=new_page_title)

        else:
            return HttpResponse("Page already exists!")

def edit_entry(request, title):

    entry_info = util.get_entry(title)

    return render(request, "encyclopedia/edit_entry.html", {
        'title' : title,
        'entry_info' : entry_info
    })


    #if (request.method == 'GET'):
    #     return render(request, "encyclopedia/edit_page.html", {
    #         "entry_info" : entry_info
    #     })
    # else:
    #     return HttpResponse("POST")

    # NOT PASSING entry info throuhg the submit button to this function????

def save_entry(request):
        return HttpResponse("saved")
