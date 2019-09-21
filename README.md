# MyCode
自制登录验证码：Ajax登录页面+pillow制作的验证码

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

简单介绍：https://www.liaoxuefeng.com/wiki/1016959663602400/1017785454949568



## 自制验证码流程

导入pillow模块：

from PIL import Image,ImageDraw,ImageFont

- 生成图片
- 生成随机字符串
- 随机字符串添加到图片上
- 将图片按图片数据返回

Image（处理图片）,ImageDraw（图片合成-给图片添加文字）,ImageFont（图片字体）

