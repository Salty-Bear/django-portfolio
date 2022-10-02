from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is about page hehe boy")

def contact(request):
    if request.method=='post':
        email=request.post['email']
        content=request.post['content']
        print(email,content)
    return render(request,'home')
