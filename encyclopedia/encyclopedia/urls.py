from django.urls import path

from . import views

# defines all urls that can be visited from this app
# when no path, run views.index function
# can give it a name to make it easier to reference from other parts of app
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create_new_page/", views.create_new_page, name="create_new_page"),
    #path("edit_entry/", views.edit_entry, name="edit_entry"),
    path("edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
    path("save_entry/", views.save_entry, name="save_entry")
]
