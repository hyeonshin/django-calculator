from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    context = {}
    return render(request, 'calculator.html', context)

def calculate(request):
    if request.method == 'POST':
        in_one = request.POST.get("in_one")
        in_two = request.POST.get("in_two")
        operation = request.POST.get('operation')
    
    if operation == "+":
        result = float(in_one) + float(in_two)
        context = {'result':result}
        return render(request, 'calculator.html', context)
    
    elif operation == "-":
        result = float(in_one) - float(in_two)
        context = {'result':result}
        return render(request, 'calculator.html', context)
    
    elif operation == "*":
        result = float(in_one) * float(in_two)
        context = {'result':result}
        return render(request, 'calculator.html', context)
    
    elif operation == "/":
        result = float(in_one) / float(in_two)
        context = {'result':result}
        return render(request, 'calculator.html', context)
    
    elif operation == "^":
        result = pow(float(in_one),float(in_two))
        context = {'result':result}
        return render(request, 'calculator.html', context)
    
    else:
        return HttpResponse('calculator.html')