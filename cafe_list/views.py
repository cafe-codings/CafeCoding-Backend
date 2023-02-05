from django.shortcuts import render, get_object_or_404
from .models import CafeInfo

def index(request):
    cafe_list = CafeInfo.objects.all()      #지역에 따라 정렬하도록 바꾸기
    context = {'cafe_list':cafe_list}
    return render(request, 'cafe_list/cafe_list.html', context)

def detail(request, cafe_list_id):
    cafe = get_object_or_404(CafeInfo, pk=cafe_list_id)
    context = {'cafe':cafe}
    return render(request, 'cafe_list/cafe_detail.html', context)
