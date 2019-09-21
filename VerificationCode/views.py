from django.shortcuts import render, HttpResponse
from MyCode import settings
import os


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        if request.POST.get('username') == 'zhaoruofei' and request.POST.get('password') == 'zhaoruofei110.':
            return HttpResponse('yes')
        else:
            return HttpResponse('no')


def index(request):
    return render(request, 'index.html')

# 验证码
def get_valid_img(request):
    import random
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    from PIL import Image, ImageDraw, ImageFont
    img_obj = Image.new('RGB', (200, 34), get_random_color())
    draw_obj = ImageDraw.Draw(img_obj)
    font_path = os.path.join(settings.BASE_DIR, 'statics/font/NAUERT__.TTF')
    print(font_path)
    font_obj = ImageFont.truetype(font_path, 16)
    sum_str = ''
    for i in range(6):
        a = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(97, 122)), chr(random.randint(65, 90))])  # 4  a  5  D  6  S
        sum_str += a
    print(sum_str)
    draw_obj.text((64, 10), sum_str, fill=get_random_color(), font=font_obj)
    from io import BytesIO
    f = BytesIO()
    img_obj.save(f, 'png')
    data = f.getvalue()

    # 验证码对应的数据保存到session里面
    request.session['valid_str'] = sum_str

    return HttpResponse(data)
