from django.shortcuts import render

# Create your views here.


def linear_graph(request):
    return render(request, 'charts/linear_graph.html')