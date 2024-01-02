from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post


def index(request):
    return render(request, 'index.html')

# 목록보기
def post_list_view(request):
    post = Post.objects.all() # 모든 글을 가져옴

    return render(request, 'posts/post_list.html', {'post': post})

# 상세보기
def post_detail_view(request, id):
    # id에 해당하는 게시글이 없으면 404 에러 반환
    post = get_object_or_404(Post, id=id)
    
    return render(request, 'posts/post_detail.html', {'post': post})

# 작성하기
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image') # image는 file로 받아야 됨
        content = request.POST.get('content')
        # created_at은 자동으로 현재 시간으로 설정
        created_at = timezone.now(),
        # 작성자는 현재 로그인한 사용자로 설정, 로그인 후 동작
        # writer = request.user,
        print(image)
        print(content)
        # print(writer)
        print(created_at)
        # data 생성
        Post.objects.create(
            image = image,
            content = content,
            # writer = writer,
            created_at = created_at,
        )
        return redirect('index')

# 수정하기
def post_update_view(request):
    return render(request, 'posts/post_form.html')

# 삭제하기
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