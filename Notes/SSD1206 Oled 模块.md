# SSD1206 Oled 模块

## 驱动安装

[Github ssd1206](https://github.com/codelectron/ssd1306)

探测 i2c 地址

```shell
i2cdetect -y -r 1
```



## 点亮

最简单的 hello word

```python
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

# substitute sh1106(...) below if using that device
device = ssd1306(port=1, address=0x3C)  # rev.1 users set port=0

with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.rectangle((0, 0, device.width, device.height), outline=0, fill=0)
	draw.text((30, 40), "Hello World", font=font, fill=255)
```

> 本质上是构造一个 [`ImageDraw`](https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html) 的对象，然后把图像刷新到 oled 里



## 显示系统信息

调用 psutil 可以在上面显示大多数系统信息

[status.py](../oled/status.py)



## 开机自动启动

[](https://forums.developer.nvidia.com/t/how-to-run-a-script-on-boot/108411/3)

总结一下就是：通过系统服务使用 `systemd` 来将在启动时调用脚本。



`lib/systemd/system/oled.service`

```shell
[Unit]
After=network.target
Description="Oled Service"
[Service]
ExecStart=/usr/local/bin/oled.sh
User=hb
[Install]
WantedBy=multi-user.target
```



[oled.sh](../oled/oled.sh)

