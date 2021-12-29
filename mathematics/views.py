from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import numpy as np


def simultaneous_eqn(request):
    return render(request, 'mathematics/simultaneous_eqn.html')


class SimultaneousEqn(View):
    def get(self, request):
        a1 = int(request.GET.get('a', None))
        b1 = int(request.GET.get('b', None))
        c1 = int(request.GET.get('c', None))
        a2 = int(request.GET.get('p', None))
        b2 = int(request.GET.get('q', None))
        c2 = int(request.GET.get('r', None))

        # USING CRAMER’S RULE…
        D = (a1 * b2) - (a2 * b1)
        Dx = (c1 * b2) - (c2 * b1)
        Dy = (a1 * c2) - (a2 * c1)
        x = Dx / D
        y = Dy / D
        unknown_1 = round(x, 4)
        unknown_2 = round(y, 4)
        data = {
            'unknown_1': unknown_1, 'unknown_2': unknown_2
        }
        return JsonResponse(data)


def simultaneous_3_eqn(request):
    return render(request, 'mathematics/simultaneous_3_eqn.html')


class SimultaneousThreeEqn(View):
    def get(self, request):
        a1 = int(request.GET.get('a1', None))
        b1 = int(request.GET.get('b1', None))
        c1 = int(request.GET.get('c1', None))
        d1 = int(request.GET.get('d1', None))
        a2 = int(request.GET.get('a2', None))
        b2 = int(request.GET.get('b2', None))
        c2 = int(request.GET.get('c2', None))
        d2 = int(request.GET.get('d2', None))
        a3 = int(request.GET.get('a3', None))
        b3 = int(request.GET.get('b3', None))
        c3 = int(request.GET.get('c3', None))
        d3 = int(request.GET.get('d3', None))

        A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        b = np.array([d1, d2, d3])
        x = np.linalg.solve(A, b)

        unknown_1 = round(x[0], 4)
        unknown_2 = round(x[1], 4)
        unknown_3 = round(x[2], 4)

        data = {
            'unknown_1': unknown_1, 'unknown_2': unknown_2, 'unknown_3': unknown_3
        }
        return JsonResponse(data)
