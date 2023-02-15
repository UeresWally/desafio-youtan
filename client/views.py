from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from .models import Client, Branch
from django.views import generic

class IndexView(generic.ListView):
    paginate_by = 4
    template_name = 'client/clients.html'
    context_object_name = 'latest_clients_list'

    def get_queryset(self):
        return Client.objects.order_by('-name')[:5]


class DetailView(generic.DetailView):
    model = Client
    template_name = 'client/detail.html'


def update_client(request, id):
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=id)
        data = request.POST
        client.active = data['active']
        client.name = data['name']
        client.save()

        return JsonResponse({'name': client.name})
    else:
        return JsonResponse('404')


def delete_client(request, id):
    if request.method == 'DELETE':
        client = get_object_or_404(Client, pk=id)
        client.delete()

        return JsonResponse('200')
    else:
        return JsonResponse('400')


def create_client_branch(request, id):
    if request.method == 'POST':

        data = request.POST
        client = get_object_or_404(Client, pk=id)
        active = True if data['active'] == 'True' else False
        branch_dict = {
            'name': data['name'],
            'active': active,
            'cnpj': data['cnpj'],
            'client_id': client
        }
        branch = Branch.objects.create(**branch_dict)
        branch.save()
        return JsonResponse({'name': client.name})
    else:
        return JsonResponse('400')


def new_client(request):
    if request.method == "POST":
        # get the form data
        data = request.POST
        # save the data and after fetch the object in instance
        active = True if data['active'] == 'True' else False
        client_dict = {
            'name': data['name'],
            'active': active,
            'cnpj': data['cnpj'],
        }
        client = Client.objects.create(**client_dict)
        client.save()
        
        # send to client side.
        return JsonResponse({"name": client.name}, status=200)
    else:
        # some form errors occured.
        return JsonResponse("400")
