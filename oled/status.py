import time
import psutil
import datetime

from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont

device = ssd1306(port=1, address=0x3C)  # rev.1 users set port=0
download_old, upload_old = 0, 0


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
    try:
        return psutil.net_if_addrs()['eth0'][0].address
    except KeyError:
        return psutil.net_if_addrs()['wlan0'][0].address


def get_temp():
    return psutil.sensors_temperatures()['thermal-fan-est'][0][1]


def layout(draw, pos, gap, content_l, content_r, font):
    draw.text(pos, str(content_l), font=font, fill=255)
    draw.text((pos[0] + gap, pos[1]), str(content_r), font=font, fill=255)


def update_network(upload, download):
    global upload_old
    upload_new = psutil.net_io_counters().bytes_sent
    uploaded = upload_new-upload_old
    upload.pop(0)
    upload.append(uploaded)
    upload_old = upload_new
    global download_old
    download_new = psutil.net_io_counters().bytes_recv
    downloaded = download_new-download_old
    download.pop(0)
    download.append(downloaded)
    download_old = download_new
    return uploaded, downloaded

def humanbytes(B):
   KB = float(1024)
   MB = float(KB ** 2)
   if B < KB:
      return f'{B} B'
   elif KB <= B < MB:
      return f'{B/KB:.2f} K'
   elif MB <= B:
      return f'{B/MB:.2f} M'
    


if __name__ == "__main__":
    font_mc = "/home/hb/Projects/HB-Nano/oled/fonts/Minecraft.ttf"
    font_retro = "/home/hb/Projects/HB-Nano/oled/fonts/retro_computer_personal_use.ttf"
    font1 = ImageFont.truetype(font_retro, 14)
    font2 = ImageFont.truetype(font_retro, 7)
    # font3 = ImageFont.truetype("/home/hb/Projects/HB-Nano/oled/fonts/FZXIANGSU12.TTF", 12)
    # font3 = ImageFont.truetype("/home/hb/Projects/HB-Nano/oled/fonts/FZJCXS.TTF", 34)
    boot_time = psutil.boot_time()
    with canvas(device) as draw:
        draw.text((6, 20), "HB-Nano",
                  font=ImageFont.truetype(font_mc, 28), fill=255)
    time.sleep(3)
    D = [0 for _ in range(60)]
    U = [0 for _ in range(60)]
    upload_old = psutil.net_io_counters().bytes_sent
    download_old = psutil.net_io_counters().bytes_recv
    while True:
        with canvas(device) as draw:
            # the out box
            draw.rectangle(
                (0, 0, device.width-1, device.height-1), outline=1, fill=0)

            # ip
            draw.text((10, -2), f'{get_host_ip()}', font=font1, fill=255)

            # uptime
            uptime = str(datetime.timedelta(seconds=int(time.time()-boot_time))
                         ).replace(" day", "d").replace(",", "").replace("s", "")
            if len(uptime) > 8:
                uptime = uptime[:-3]
            draw.text((8, 13), f'ONLINE  FOR  {uptime}', font=font2, fill=255)

            # 4 system status
            # CPU | TEMP
            # MEM | DISK
            status_x = 7
            status_y = 20
            layout(draw, (status_x, status_y), 20, 'CPU', f':{psutil.cpu_percent():.1f}%', font2)
            layout(draw, (status_x, status_y + 7), 20, 'MEM', f':{psutil.virtual_memory().percent:.1f}%', font2)
            layout(draw, (status_x + 60, status_y), 27, 'TEMP', f':{get_temp():.1f}', font2)
            layout(draw, (status_x + 60, status_y + 7), 27, 'DISK', f':{psutil.disk_usage("/").percent:.0f} %', font2)
            

            # network
            upload_speed, download_speed = update_network(U, D)
            layout(draw, (status_x, status_y + 14), 10, 'U:', f'{humanbytes(upload_speed)}'.replace('.', ' .'), font2)
            layout(draw, (status_x + 60, status_y + 14), 10, 'D:', f'{humanbytes(download_speed)}'.replace('.', ' .'), font2)

            U_max = max(U) if max(U) > 1000 else 1000
            D_max = max(D) if max(D) > 1000 else 1000
            draw.line(list(zip(range(2, 62), [61-15*u/U_max for u in U])), fill=255)
            draw.line(list(zip(range(65, 125), [61-15*d/D_max for d in D])), fill=255)
            

            # others
            # draw.text((8, 20), "全场起立，卢本伟牛逼！", font=font3, fill=255)

        time.sleep(1)
