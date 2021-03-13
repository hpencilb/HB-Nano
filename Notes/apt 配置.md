# apt 配置

`/etc/apt/sources.list`

```shell
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu-ports/ bionic-security main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-updates main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-backports main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu-ports/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-proposed main restricted universe multiverse

```

