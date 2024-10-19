from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("profilePage/", profilePage, name="profilePage"),
    
    
    path("addBlogPage/", addBlogPage, name="addBlogPage"),
    path("createdBlogBy/", createdBlogBy, name="createdBlogBy"),
    
    path("editBlog/<str:blog_id>", editBlog, name="editBlog"),
    path("deleteBlog/<str:blog_id>", deleteBlog, name="deleteBlog"),
    path("viewSingleBlog/<str:blog_id>", viewSingleBlog, name="viewSingleBlog"),
    
    path("AllBlogPost/", AllBlogPost, name="AllBlogPost"),
    path("search_blog/", search_blog, name="search_blog"),
    path("editProfilePage/", editProfilePage, name="editProfilePage"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
