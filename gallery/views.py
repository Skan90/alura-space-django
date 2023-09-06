from django.shortcuts import render


def index(request):

    data = {
        1: {"name": "Nebulosa Eta Carinae",
            "description": "webbtelecope.org / NASA / James Webb Space Telescope"},
        2: {"name": "Galaxy NGC 1079",
            "description": "nasa.org / NASA / Hubble Space Telescope"},
    }

    return render(request, 'gallery/index.html', {"cards": data})


def imagem(request):
    return render(request, 'gallery/imagem.html')