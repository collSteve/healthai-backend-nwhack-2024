from django.shortcuts import render
from django.http import HttpResponse

# Post request for health instruction
def health_instruction(request):
    if request.method == 'GET':
        return HttpResponse('Hello, World!')
    else:
        return render(request, 'health_instruction.html')