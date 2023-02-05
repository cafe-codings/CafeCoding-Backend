from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 Cafe Coding 홈페이지입니다.")