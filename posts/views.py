from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView

from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image') # image는 file로 받아야 됨
        content = request.POST.get('content')
        writer = request.POST.get('writer')
        print(image)
        print(content)
        print(writer)
        # data 생성
        Post.objects.create(
            image = image,
            content = content,
            writer = request.user # 로그인 후 동작됨
        )
        return redirect('index')

def post_update_view(request):
    return render(request, 'posts/post_form.html')

def post_delete_view(request):
    return render(request, 'posts/post_confirm_delete.html')

# def url_view(request):
#     print('url_view()')
#     data = {'code': '001', 'msg': 'OK'}
#     # return HttpResponse('<h1>url_view</h1>')
#     return JsonResponse(data) # Json 형식

# def url_parameter_view(request, username):
#     print('url_parameter_view()')
#     print(f'username: {username}')
#     print(f'request.GET: {request.GET}')
#     return HttpResponse(username)

# def function_view(request):
#     print(f'request.method: {request.method}')
#     # 데이터를 받을 때 ex) 데이터 검색
#     if request.method == 'GET':
#         print(f'request.GET: {request.GET}')

#     # 데이터를 추가나 생성할 때, ex) 회원가입
#     elif request.method == 'POST':
#         print(f'request.POST: {request.POST}') 
#     return render(request, 'view.html')