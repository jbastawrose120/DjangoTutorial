from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,'basicApp/index.html',context_dict)

def other(reqeust):
    return render(reqeust,'basicApp/other.html')

def relative(reqeust):
    return render(reqeust,'basicApp/relative_url_templates.html')
