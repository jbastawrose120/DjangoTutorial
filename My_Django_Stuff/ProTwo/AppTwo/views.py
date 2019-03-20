from django.shortcuts import render
#from django.http import HttpResponse
#from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.
# def help(request):
#     my_dict = {'help_stuff' : "Welcome to the help page! (From AppTwo/help.html)"}
#     return render(request,'AppTwo/help.html',context=my_dict)

#Code from example project
# webpages_list = AccessRecord.objects.order_by('date')
# date_dict={'access_records':webpages_list}
# return render(request,'first_app/index.html',context=date_dict)

def users(request):
    #return render(request, 'AppTwo/users.html')
    # user_list = User.objects.order_by('last_name')
    # user_dict={'user_records':user_list}
    # return render(request, 'AppTwo/users.html', context=user_dict)
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR: FORM INVALID')

    return render(request, 'AppTwo/users.html', {'form':form})



def index(request):
    return render(request, 'AppTwo/index.html')
