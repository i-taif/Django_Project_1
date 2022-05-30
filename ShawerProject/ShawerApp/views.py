from django.shortcuts import get_object_or_404, redirect, render,redirect
from .models import counselor, comment
from .forms import CommentForm

# Create your views here.
def home(request):
    return render(request,'index.html',{'title':'home'})
def about(request):
    return render(request,'about.html')

def consolt(request):
    context= { 'consoler':counselor.objects.all(),}
    return render(request,'counsolting.html',context)

def delete(request, list_id):
    item = comment.objects.get(pk=list_id)
    item.delete()
    return redirect('home')

def courses(request):
    return render(request,'courses.html')
    

def comment_detile(request, pk):
   # profile=counselor.objects.get(pk=pk)
    profile=get_object_or_404(counselor, pk=pk)
    if request.method=='POST':
       form= CommentForm(request.POST)

       if form.is_valid():
          obj= form.save(commit=False)
          obj.profile=profile
          obj.save()

          return redirect('profile',pk=profile.pk)
    else:
        form= CommentForm()

    context={
        'profile':profile,
        'form':form}
    return render(request,'profile.html',context)

