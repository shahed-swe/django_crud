from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from crud.models import Information
from crud.forms import InformationModelForm
# Create your views here.

def info_form(request):
    if request.method == 'POST':
        form = InformationModelForm(request.POST)
        if form.is_valid():
            try:
                f_pass = form.cleaned_data['password_first']
                l_pass = form.cleaned_data['password_last']
                if f_pass == l_pass:
                    form.save()
                    return redirect('/home/')
                else:
                    print("Enter Password Doesn't Match!!")
                    return redirect('/info_form/')
            except:
                pass
    else:
        form = InformationModelForm()
    return render(request, "registrationform.html", {"title":"Registration",'form': form})

def home(request):
    qs = Information.objects.all()
    context = {'object_list': qs,"title":"Home"}
    return render(request,'index.html',context)

def info_details(request, id):
    obj = get_object_or_404(Information, id=id)
    template_name = 'info_details.html'
    context = {"objects": obj,"title":"Details"}
    return render(request, template_name, context)

def info_update(request, id):
    obj = get_object_or_404(Information, id=id)
    form = InformationModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/home/')
    template_name = 'update.html'
    context = {'form': form,"title":f"update {obj.first_name}"}
    return render(request, template_name, context)

def info_delete(request, id):
    obj = get_object_or_404(Information, id=id)
    template_name = 'delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/home/')
    context = {'objects': obj,"title":f"update {obj.first_name}"}
    return render(request, template_name,context)