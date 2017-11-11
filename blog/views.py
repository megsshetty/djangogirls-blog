from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Blog

def fun(request):
    #newblog = Blog.objects.create(title="1",content="this is some random data. Dont care about it.")
    #print(newblog.title)
    blogs=Blog.objects.all()
    return render(request,'bloglist.html',{"blogs":blogs})

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        abstract = request.POST.get("abstract")
        Blog.objects.create(title=title,content=content)
    return render(request,'blogcreate.html')

def edit(request,blogid):
    blog = Blog.objects.get(id=blogid)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        abstract = request.POST.get("abstract")
        blog.title = title
        blog.content = content
        blog.abstract = abstract
        blog.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,'blogedit.html',{"blog":blog})





def delete(request,blogid):
    blog = Blog.objects.get(id=blogid)
    blog.delete()
    return HttpResponseRedirect("/")
