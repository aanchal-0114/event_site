from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import event_template,like_template
from django.contrib import messages
import json
# Create your views here.
def index(request):
    event = event_template.objects.all()
    c=0
    if request.is_ajax:
        pid=request.POST.get('pid')
        like = like_template.objects.all()
        for i in like:
            if(i.ids == pid):
                obj = like_template.objects.filter(ids=pid)
                obj.delete()
                c=1
                break
        
        if(c==0):
            obj = event_template.objects.filter(pid=pid)
            for i in obj:
                like = like_template(ids=i.pid,day=i.day,month=i.month,start_time=i.start_time, end_time=i.end_time, location=i.location , name=i.name ,image1 = i.image1)
                like.save()

    like = like_template.objects.all()
    value =[]
    for i in like:
        value.append(i.ids)
    value = json.dumps(value)
    params = {'event':event,'value':value}
    return render(request,'index.html',params); 

def like(request):
    like = like_template.objects.all()
    params = {'like':like} 
    return render(request,'like_event.html',params)


def event_register(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        day = request.POST.get('day','')
        month = request.POST.get('month','')
        start_time = request.POST.get('start','')
        end_time = request.POST.get('end','')
        location = request.POST.get('loc','')
        image1 = request.FILES.get('product_image1','')
        event = event_template(name=name,day=day,month=month,start_time=start_time,end_time=end_time,location=location,image1=image1)
        event.save()
        messages.success(request,"Thanks for registering your event , we are glad!")
        return redirect('http://127.0.0.1:8000/event_register/')
    return render(request,'event_register.html')