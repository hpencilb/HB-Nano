# apt 配置

`sudo vim /etc/apt/sources.list`

```shell
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu-ports/ bionic-security main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-updates main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-backports main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-security main restricted universe multiverse

# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-proposed main restricted universe multiverse
```


