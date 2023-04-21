from django.urls import path
from .import views
urlpatterns = [
   path("blog/",views.ShowBlog, name='showblog'),
   path("",views.ShowHome, name='showhome'),
   path("contact/",views.ShowContact, name='showcontact'),
   path("about/",views.ShowAbout, name='showabout'),
   path("insertdata/",views.InsertData, name='insertdata'),
]