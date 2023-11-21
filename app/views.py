from django.shortcuts import render

# Create your views here.
def ind(request):
    return render(request,'ind.html')

def aus(request):
    return render(request,'aus.html')