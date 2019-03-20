from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content' : "HELLO IM FROM FIRST APP"}
    return render(request, 'leveltwo_firstapp/index.html', context=my_dict)
