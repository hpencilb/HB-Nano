# Wi-Fi 配置

> mt7601u USB 网卡

## ~~驱动安装~~

~~[Ralink MT7601U (148f:7601) Wi-Fi adapter installation](https://askubuntu.com/questions/457061/ralink-mt7601u-148f7601-wi-fi-adapter-installation)~~

```shell
sudo apt-get install linux-headers-generic build-essential git
git clone https://github.com/art567/mt7601usta.git
cd mt7601usta/src 
sudo make
sudo make install
sudo mkdir -p /etc/Wireless/RT2870STA/
sudo cp RT2870STA.dat /etc/Wireless/RT2870STA/
sudo modprobe mt7601Usta
```

~~升级后使用~~

```shell
cd mt7601/src
make clean
make
sudo make install
sudo modprobe mt7601Usta
```

> [Existing Linux Wireless drivers](https://wireless.wiki.kernel.org/en/users/drivers)
> 
> **Linux 内核中包含了对 mt7601u 的驱动，不需要手动安装。**

## 配置 Wi-Fi

[Debian 或 Ubuntu 在命令行下配置无线网络连接 WiFi 的方法](https://wenqixiang.com/linux-wireless-configuration-in-terminal-command-line/)

[Linux 的WiFi命令行配置](https://my.oschina.net/u/2306127/blog/1587353)

[Linux 手动无线网卡 WiFi 配置](https://blog.csdn.net/vic_qxz/article/details/88658802)

[树莓派连接Wi-Fi](https://www.jianshu.com/p/a2eb6a24a2d0)

设置 `/etc/wpa_supplicant/seu-wlan.conf` 为

```shell
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="seu-wlan"
    psk="密码"
}
```

一定要 `sudo` 来运行

```shell
sudo wpa_supplicant -B -i wlan0 -c /etc/seu-wlan.conf
sudo dhclient wlan0
```

## 设置开机自动连接

[How can I enable wpa_supplicant on boot?](https://unix.stackexchange.com/questions/173781/how-can-i-enable-wpa-supplicant-on-boot)

>  [How to autorun wpa_supplicant on Debian startup](https://superuser.com/questions/412566/how-to-autorun-wpa-supplicant-on-debian-startup)

```shell
allow-hotplug wlan0
iface wlan0 inet dhcp
    wpa-conf /etc/seu-wlan.conf
```
