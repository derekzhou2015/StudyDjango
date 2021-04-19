from django.shortcuts import render, HttpResponse, redirect
from .models import Account, AccountDetails
from .form import AccountForm, AccountEditForm
from json import loads
# Create your views here.


def index(request):
    l1 = Account.objects.all().order_by('-id')
    return render(request, 'Account/index.html', {'context': l1})


def add(request):
    if request.method == 'GET':
        form = AccountForm()
        return render(request, 'Account/add.html', {'form': form})
    else:
        form = AccountForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            acc_details = AccountDetails()
            acc_details.gender = data['gender']
            acc_details.tel = data['tel']
            acc_details.addr = data['addr']
            acc_details.birthday = data['birthday']
            acc_details.save()

            acc = Account()
            acc.first_name = data['first_name']
            acc.last_name = data['last_name']
            acc.email = data['email']
            acc.password = data['password']
            acc.acc_details = acc_details
            acc.save()
            return redirect('../')
        else:
            return render(request, 'Account/add.html', {'form': form})


def edit(request):
    obj = Account.objects.get(pk=request.GET['id'])
    if request.method == 'GET':
        form = AccountEditForm({
            'id': obj.id,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'password': obj.password,
            'gender': obj.acc_details.gender,
            'tel': obj.acc_details.tel,
            'addr': obj.acc_details.addr,
            'birthday': str(obj.acc_details.birthday)
        })
    else:
        form = AccountEditForm(request.POST)
        print(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            obj.acc_details.gender = data['gender']
            obj.acc_details.tel = data['tel']
            obj.acc_details.addr = data['addr']
            obj.acc_details.birthday = data['birthday']
            obj.acc_details.save()

            obj.first_name = data['first_name']
            obj.last_name = data['last_name']
            obj.email = data['email']
            obj.password = data['password']
            obj.acc_details = obj.acc_details
            obj.save()
            return redirect('../')
    return render(request, 'Account/add.html', {'form': form, 'edit': True})


def delete(request):
    id = request.GET['id']
    account = Account.objects.get(pk=id)
    AccountDetails.objects.get(account=account).delete()

    return redirect('../')
