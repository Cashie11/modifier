from django.shortcuts import render, get_object_or_404
from .models import UserData
import random
import string

def generate_code():
    code_length = 10
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ''.join(random.choice(chars) for _ in range(code_length))
    return code

def index(request):
    if request.method == 'POST':
        data = request.POST['data']
        code = generate_code()

        while UserData.objects.filter(code=code).exists():
            code = generate_code()

        user_data = UserData(code=code, data=data)
        user_data.save()
        
        return render(request, 'index.html', {'code': code})
    
    return render(request, 'index.html')


def retrieve_data(request):
    if request.method == 'POST':
        code = request.POST['code']
        user_data = get_object_or_404(UserData, code=code)
        return render(request, 'view_data.html', {'data': user_data.data})
    return render(request, 'view_data.html')



# Create your views here.
