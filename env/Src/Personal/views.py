from django.shortcuts import render

def crete_home_screen(request):
    print(request.headers)
    context={
        "Name":[10,20,30],
        "age" :20
    }


    return render(request,'personal/home.html',context)
