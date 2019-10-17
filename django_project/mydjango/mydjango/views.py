from django.http import HttpResponse

def show(request):
    return HttpResponse("My first Django project")

def main(request):
    return HttpResponse("My main page.")
    
def show_03(request, year, month, day):
    return HttpResponse("Birthday:"+year+"-"+month+"-"+day+".")