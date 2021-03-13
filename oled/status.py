import time
import socket
import psutil
import datetime

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont, ImageDraw

device = ssd1306(port=1, address=0x3C)  # rev.1 users set port=0


def get_host_ip():
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # for _ in range(5):
    #     try:
    #         s.connect(('8.8.8.8', 80))
    #         ip = s.getsockname()[0]
    #         s.close()
    #         return ip
    #     except OSError:
    #         time.sleep(2)
    # return "X.X.X.X"
    return psutil.net_if_addrs()['wlan0'][0].address


def get_temp():
    return psutil.sensors_temperatures()['thermal-fan-est'][0][1]


def layout(draw, pos, gap, content_l, content_r, font):
    draw.text(pos, str(content_l), font=font, fill=255)
    draw.text((pos[0] + gap, pos[1]), str(content_r), font=font, fill=255)


if __name__ == "__main__":
    font_mc = "/home/hb/Projects/oled/fonts/Minecraft.ttf"
    font_retro = "/home/hb/Projects/oled/fonts/retro_computer_personal_use.ttf"
    font1 = ImageFont.truetype(font_retro, 14)
    font2 = ImageFont.truetype(font_retro, 7)
    # font3 = ImageFont.truetype("/home/hb/Projects/oled/fonts/FZXIANGSU12.TTF", 12)
    # font3 = ImageFont.truetype("/home/hb/Projects/oled/fonts/FZJCXS.TTF", 34)
    boot_time = psutil.boot_time()
    with canvas(device) as draw:
        draw.text((6, 20), "HB-Nano", font=ImageFont.truetype(font_mc, 28), fill=255)
    time.sleep(3)
    while True:
        with canvas(device) as draw:
            # the out box
            draw.rectangle((0, 0, device.width-1, device.height-1), outline=1, fill=0)

            # ip
            draw.text((10, -2), f'{get_host_ip()}', font=font1, fill=255)

            # uptime
            draw.text((8, 13), f'ONLINE  FOR  {str(datetime.timedelta(seconds=int(time.time()-boot_time)))}', font=font2, fill=255)

            # 4 system status
            status_x = 7
            status_y = 20
            layout(draw, (status_x, status_y + 7), 20, 'CPU', f':{psutil.cpu_percent():.1f}%', font2)
            layout(draw, (status_x, status_y), 20, 'MEM', f':{psutil.virtual_memory().percent:.1f}%', font2)
            layout(draw, (status_x + 60, status_y + 7), 27, 'DISK', f':{psutil.disk_usage("/").percent:.0f} %', font2)
            layout(draw, (status_x + 60, status_y), 27, 'TEMP', f':{get_temp():.1f}', font2)



            # others
            # draw.text((8, 20), "全场起立，卢本伟牛逼！", font=font3, fill=255)
        time.sleep(1)
