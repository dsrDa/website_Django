from django.shortcuts import render

# Create your views here.

def design_ltda_index(request):
    return render(
        request,
        "index.html"
    )

def design_ltda_elementos_design(request):
    return render(
        request,
        "elementos_design.html"
    )

def design_ltda_contatos(request):
    return render(
        request,
        "contatos.html"
    )