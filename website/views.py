from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.

# def test(request):
#     now = datetime.now()
#
#     return render(
#         request,
#         'website/test.html',
#         context = {
#         "now": now
#         }
#     )


def home(request):
    return render(
        request,
        'website/index.html'

    )

