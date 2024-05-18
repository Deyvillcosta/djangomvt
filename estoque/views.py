from django.shortcuts import render, redirect
from .models import Estoque
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        if((request.POST.get('upid') == None) and (request.POST.get('delid') == None )):
                it_nome = request.POST.get('nome')
                it_qntd = request.POST.get('quantidade')
                it_marca = request.POST.get('marca')
                it_precounid = request.POST.get('precounid')
                it_precounid = it_precounid.replace(',', '.')
                it_precounid = float(it_precounid)
                it_qntd = int(it_qntd)

                item = Estoque(nome=it_nome, marca=it_marca, quantidade=it_qntd, precounid=it_precounid)
                item.save()

                messages.success(request, 'Item adicionado!')
                it_nome = ""
                it_qntd = ""
                it_marca = ""
                it_precounid = ""
                return redirect("home")


        elif(request.POST.get('upid') != None):
                it_id = request.POST.get('upid')
                it_id = int(it_id)
                item= Estoque.objects.get(id=it_id)

                if request.POST.get('nome') != "":
                    item.nome = request.POST.get('nome')
                if request.POST.get('quantidade') != "":
                    it_qntd = request.POST.get('quantidade')
                    it_qntd = int(it_qntd)
                    item.quantidade = it_qntd
                if request.POST.get('precounid') != "":
                    it_precounid = request.POST.get('precounid').replace(',', '.')
                    item.precounid = float(it_precounid)

                item.save()
                messages.success(request, 'Item atualizado!')
                return redirect("home")


        elif(request.POST.get('delid') != None):
            it_id = request.POST.get('delid')
            it_id = int(it_id)
            item = Estoque.objects.get(id=it_id)
            item.delete()
            messages.success(request, 'Item excluído!')
            return redirect("home")

    items = Estoque.objects.all()
    return render(request, 'home.html', {'items': items})




