import math
import numpy as np
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


@login_required
def simultaneous_eqn(request):
    return render(request, 'mathematics/simultaneous_eqn.html')


class SimultaneousEqn(LoginRequiredMixin, View):
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


@login_required
def simultaneous_3_eqn(request):
    return render(request, 'mathematics/simultaneous_3_eqn.html')


class SimultaneousThreeEqn(LoginRequiredMixin, View):
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


@login_required
def quadratic_eqn(request):
    return render(request, 'mathematics/quadratic_eqn.html')


class QuadraticEqn(LoginRequiredMixin, View):
    def get(self, request):
        a = int(request.GET.get('a_1', None))
        b = int(request.GET.get('b_1', None))
        c = int(request.GET.get('c_1', None))
        determinant = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(determinant))
        if determinant > 0:
            info = 'Real and different roots'
            root_1 = (-b + sqrt_val) / (2 * a)
            root_2 = (-b - sqrt_val) / (2 * a)
            data = {
                'info': info, 'root_1': root_1, 'root_2': root_2
            }
            return JsonResponse(data)
        elif determinant == 0:
            info = 'Real and same roots'
            root_1 = -b / (2 * a)
            root_2 = -b / (2 * a)
            data = {
                'info': info, 'root_1': root_1, 'root_2': root_2
            }
            return JsonResponse(data)
        else:
            info = 'Complex roots'
            root_1 = - b / (2 * a), " +i", sqrt_val
            root_2 = - b / (2 * a), " - i", sqrt_val
            data = {
                'info': info, 'root_1': root_1, 'root_2': root_2
            }
            return JsonResponse(data)


@login_required
def from_base_10(request):
    return render(request, 'mathematics/from_base_10.html')


class FromBase10(LoginRequiredMixin, View):
    def get(self, request):
        num_10 = int(request.GET.get('num_10', None))
        base = int(request.GET.get('num_x', None))
        num_to_char = {i: "0123456789ABCDEF"[i] for i in range(16)}
        power = int(math.log(num_10, base))
        converted = ""
        for pow in range(power, -1, -1):
            # divide
            converted += num_to_char[num_10 // (base ** pow)]
            # remainder
            num_10 %= base ** pow
        data = {
            'value': converted
        }
        return JsonResponse(data)


@login_required
def to_base_10(request):
    return render(request, 'mathematics/to_base_10.html')


class ToBase10(LoginRequiredMixin, View):
    def get(self, request):
        number = request.GET.get('number', None)
        base = int(request.GET.get('base', None))

        converted = int(number, base)
        data = {
            'converted': converted
        }
        return JsonResponse(data)


def from_base_10_func(num, base):
    numToChar = {i: "0123456789ABCDEF"[i] for i in range(16)}

    # set power to largest
    power = int(math.log(num, base))

    # convert numbers
    converted = ""
    for pow in range(power, -1, -1):
        # divide
        converted += numToChar[num // (base ** pow)]
        # remainder
        num %= base ** pow
    return converted


@login_required
def add_bases(request):
    return render(request, 'mathematics/add_bases.html')


class AddBases(LoginRequiredMixin, View):
    def get(self, request):
        num1 = request.GET.get('num1', None)
        base1 = request.GET.get('base1', None)
        num2 = request.GET.get('num2', None)
        base2 = request.GET.get('base2', None)
        add_base = request.GET.get('add_base', None)
        nums_list = request.GET.getlist('nums_list[]', None)
        bases_list = request.GET.getlist('bases_list[]', None)
        add_list = []
        # first convert to base 10
        number_1 = int(num1, int(base1))
        number_2 = int(num2, int(base2))
        for number, base in zip(nums_list, bases_list):
            con = int(number, int(base))
            add_list.append(con)
        print(add_list)
        add_list_sum = sum(add_list)

        # add the numbers in base 10
        add_in_10 = number_1 + number_2 + add_list_sum
        # convert to the desired base
        sum_con = from_base_10_func(add_in_10, int(add_base))

        data = {
            'result': sum_con
        }
        return JsonResponse(data)


@login_required
def subtract_bases(request):
    return render(request, 'mathematics/subtract_bases.html')


class SubtractBases(LoginRequiredMixin, View):
    def get(self, request):
        sub_num1 = request.GET.get('sub_num1', None)
        sub_base1 = request.GET.get('sub_base1', None)
        sub_num2 = request.GET.get('sub_num2', None)
        sub_base2 = request.GET.get('sub_base2', None)
        subtract_base = request.GET.get('subtract_base', None)
        # sub_nums_list = request.GET.getlist('sub_nums_list[]', None)
        # sub_bases_list = request.GET.getlist('sub_bases_list[]', None)
        # subtract_list = []
        # first convert to base 10
        number_1 = int(sub_num1, int(sub_base1))
        number_2 = int(sub_num2, int(sub_base2))
        # for number, base in zip(sub_nums_list, sub_bases_list):
        #     con = int(number, int(base))
        #     subtract_list.append(con)
        # print(subtract_list)
        # subtract_list_sum = sum(subtract_list)

        # subtrace the numbers in base 10
        add_in_10 = number_1 - number_2
        # convert to the desired base
        subtract_con = from_base_10_func(add_in_10, int(subtract_base))

        data = {
            'result': subtract_con
        }
        return JsonResponse(data)


@login_required
def multiply_bases(request):
    return render(request, 'mathematics/multiply_bases.html')


@login_required
def calculator(request):
    return render(request, 'mathematics/calculator.html')
