from django.shortcuts import render
from .service import GitHub
from django.conf import settings

def criar_chamado(request):

    if request.method == "POST":

        github = GitHub(settings.USERNAME, settings.PASSWORD)
        github.access(settings.REPOSITORY, settings.OWNER)

        retorno = github.create_issue(
                    title=request.POST.get("titulo"), 
                    autor=request.POST.get("autor"),
                    setor=request.POST.get("setor"),
                    conteudo=request.POST.get("conteudo")
                )
    else:
        retorno = None

    return render(request,"index.html",{"retorno":retorno})