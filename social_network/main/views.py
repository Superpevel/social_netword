from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})