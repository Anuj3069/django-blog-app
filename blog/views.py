from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 

# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3) 
    page_number=request.GET.get('page') 
    try: 
     post_list=paginator.page(page_number) 
    except PageNotAnInteger: 
     post_list=paginator.page(1) 
    except EmptyPage: 
     post_list=paginator.page(paginator.num_pages) 
    return render(request,'blog/post_list.html',{'post_list':post_list})


def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='publish',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    return render(request,'blog/post_detail.html',{'post':post})       

from django.core.mail  import send_mail
from blog.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='publish')
    form=EmailSendForm()
    return render(request,'blog/sharebyemail.html',{'form':form,'post':post}) 