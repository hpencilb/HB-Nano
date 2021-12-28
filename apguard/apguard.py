#!/usr/bin/python3
import socket
import subprocess as sb
import time

import psutil


def guard():
    network = psutil.net_if_addrs()
    ap_status = sb.run(('service', 'hostapd', 'status')).returncode
    should_turn_on = False
    try:
        usb_wifi = network['wlx00e02d40699d']
        if not any(net.family is socket.AF_INET for net in usb_wifi):
            should_turn_on = True
    except KeyError:
        should_turn_on = True

    if should_turn_on:
        if ap_status != 0:
            sb.run(('service', 'hostapd', 'start'))
    else:
        if ap_status == 0:
            sb.run(('service', 'hostapd', 'stop'))


if __name__ == '__main__':
    while True:
        guard()
        time.sleep(15)
