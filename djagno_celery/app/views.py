from django.shortcuts import render
from app.tasks import add
# from djagno_celery.celery import sub
from celery.result import AsyncResult


# Enqueue task using delay()
# def Home(request):
#     # add.delay(10,20)
#     res = add.delay(10,20)
#     print("result1",res)
#     res2 = sub.delay(30,20)
#     print("result2",res2)
# return render(request,"home.html")

#Enqueue taks using apply_async()
# def Home(request):
#     # add.delay(10,20)
#     res = add.apply_async(args=[10,20])
#     print("result1",res)
#     res2 = sub.apply_async(args=[30,20])
#     print("result2",res2)
#     return render(request,"home.html")
    
# display value after taks execution
def Home(request):
    res = add.delay(10,20)
    return render(request,"home.html",{"result":res})

def show_result(request,res_id):
    result = AsyncResult(res_id)
    print("Ready :",result.ready())
    print("Successful :",result.successful())
    print("Failed :",result.failed())
    
    return render(request,"result.html",{"result":result})

def About(request):
    return render(request,"about.html")


def Contact(request):
    return render(request,"contact.html")