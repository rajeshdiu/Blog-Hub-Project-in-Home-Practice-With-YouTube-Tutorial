from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.db.models import Q


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        gender=request.POST.get("gender")
        age=request.POST.get("age")
        contact_no=request.POST.get("contact_no")
        profile_pic=request.FILES.get("profile_pic")
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Age=age,
                Contact_No=contact_no,
                Gender=gender,
                profile_pic=profile_pic,
            )
            
            if user_type=='viewers':
                viewersProfileModel.objects.create(user=user)
                
            elif user_type=='blogger':
                BloggerProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

def profilePage(request):
    
    return render(request,"profilePage.html")


def addBlogPage(request):
    
    current_user=request.user
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        
        return redirect("createdBlogBy")
        
    
    return render(request,"addBlogPage.html")


def createdBlogBy(request):
    
    current_user=request.user
    
    blog=BlogPostModel.objects.filter(user=current_user)
    
    context={
        'blog':blog
    }
    
    
    return render(request,"createdBlogBy.html",context)


def deleteBlog(request,blog_id):
    
    
    blog=BlogPostModel.objects.get(id=blog_id).delete()
    
    return redirect("createdBlogBy")


def viewSingleBlog(request,blog_id):
    
    
    blog=BlogPostModel.objects.get(id=blog_id)
    
    context={
        'blog':blog
    }
    
    return render(request,"viewSingleBlog.html",context)


def editBlog(request,blog_id):
    
    blog=BlogPostModel.objects.get(id=blog_id)
    
    current_user=request.user
    
    if request.method == 'POST':
        blogid = request.POST['blogid']
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            id=blogid,
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        
        return redirect("createdBlogBy")
    
    context={
        'blog':blog
    }
    
    
    return render(request,"editBlog.html",context)


def AllBlogPost(request):
    
    blog=BlogPostModel.objects.all()
    
    context={
        'blog':blog
    }
    
    return render(request,"AllBlogPost.html",context)


def search_blog(request):
    
    query = request.GET.get('query')
    
    print(query)
    
    if query:
         blog = BlogPostModel.objects.filter(Q(BlogTitle__icontains=query) 
                                       |Q(Category__icontains=query) 
                                       |Q(BlogBody__icontains=query) 
                                       |Q(user__username__icontains=query)
                                       )
    else:
        blog = BlogPostModel.objects.none()
        
    context={
        'blogs':blog,
        'query':query
    }
    
    
    return render(request,"search_blog.html",context)


def editProfilePage(request):
    
    current_user=request.user
    
    if request.method=='POST':
        #basic_information
        
        current_user.username=request.POST.get("username")
        current_user.first_name=request.POST.get("first_name")
        current_user.last_name=request.POST.get("last_name")
        current_user.email=request.POST.get("email")
        current_user.gender=request.POST.get("gender")
        current_user.age=request.POST.get("age")
        current_user.contact_no=request.POST.get("contact_no")
        current_user.profile_pic=request.FILES.get("profile_pic")
        current_user.save()
        
        try:  
            viewersprofile=viewersProfileModel.objects.get(user=current_user)
            
            viewersprofile.Bio=request.POST.get("bio")
            viewersprofile.interests=request.POST.get("interests")
            viewersprofile.preferred_content_type=request.POST.get("preferred_content_type")
            viewersprofile.location=request.POST.get("location")
            
            viewersprofile.save()
            
            return redirect("profilePage")
            
        except viewersProfileModel.DoesNotExist:
            viewersprofile=None
        
        try:  
            bloggersprofile=BloggerProfileModel.objects.get(user=current_user)
            
            bloggersprofile.Bio=request.POST.get("bio")
            bloggersprofile.website_url=request.POST.get("website_url")
            bloggersprofile.location=request.POST.get("location")
            
            bloggersprofile.save()
            
            return redirect("profilePage")
            
        except BloggerProfileModel.DoesNotExist:
            bloggersprofile=None
    
    return render(request,"editProfilePage.html")
    
    