from django.db import models
from django.utils import timezone

class CafeInfo(models.Model):
    cafeName = models.CharField(max_length=100) #이름
    location = models.CharField(max_length=10, default = '서울')    # 위치(시군구)
    cafe_address = models.TextField(default= '서울시')           # 주소
    cafe_floors = models.TextField(default = '1층')            # 규모(층수, 별관)
    businiess_time = models.TextField(default='매일 영업')      # 운영 시간(요일별로 하면 될듯)
    complexity = models.TextField(default = '쾌적')             # 혼잡도
    price_range = models.TextField(default = '저렴')            # 가격대
    furniture_feature = models.TextField(default = '나무의자')   # 책상 및 의자 특징
    socket_existence = models.BooleanField(default = True)      #콘센트 유무
    socket_amount = models.IntegerField(default = '5')          #콘센트 개수(적음/보통/많음/매우많음)
    wifi_existence = models.BooleanField(default =True)         # 와이파이 유무
    wifi_speed = models.IntegerField(default = '3')             # 와이파이 속도(느림/보통/쾌적함/빠름) -> 5개로 나눠서 하면 될 듯
    features = models.TextField(default = '노키즈존 존재')       #기타 특징
    update_date = models.DateField(default =timezone.now())            #업데이트 날짜
    
    def __str__(self):
        return self.cafeName
    # Cafe URL, 규모, 운영 시간, 혼잡도, 가격대, 책상 및 의자 특징 수정 필요
