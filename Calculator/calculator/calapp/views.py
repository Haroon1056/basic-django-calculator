from django.shortcuts import render

def calculator(request):
    c = ''
    try:
        if request.method=="POST":
            val1= eval(request.POST.get('val1'))
            val2= eval(request.POST.get('val2'))
            opt= request.POST.get('opt')
            if opt=="+":
                c = val1 + val2
            elif opt=="-":
                c = val1 - val2
            elif opt=="*":
                c = val1 * val2
            elif opt=="/":
                c = val1 / val2
    except:
        c = "invalid operation..."
    return render(request, "calculator.html",{'c': c})
