# 主题

乾颐堂 现任明教教主 网络设备自动化高级封装

## 项目描述

qyt_devnet是我做的一个简单的华为自动化项目, 可以直接pip install qyt_devnet使用, 如果大家觉得好我可以维护更新这个项目, 加入更多华为设备的支持! 其实非华为的设备用netmiko就好了! 由于华为不受人待见,大家都不支持, 只有自己搞一个了


## 作业

乾颐堂 现任明教教主 [YouTube首页](https://www.youtube.com/channel/UCsvHsD_g8j2IEZDlVzMC3Qw)

## 使用案例

# SNMP
from qyt_devnet.qyt_snmp import QYTHuaweiSNMP
r1 = '192.168.1.151'
community_ro = "QytangR0"
snmp_client = QYTHuaweiSNMP(r1, community_ro)
\# 系统描述
print(snmp_client.sys_desc())
# 主机名
print(snmp_client.hostname())
# 地点
print(snmp_client.location())
# CPU利用率
print(snmp_client.cpu_usage())
# 内存利用率
print(snmp_client.mem_usage())
# 接口清单
print(snmp_client.get_ifs())
# 接口速率
print(snmp_client.get_if_speed())
# 接口入向字节数
print(snmp_client.get_if_in_bytes())
# 接口出向字节数
print(snmp_client.get_if_out_bytes())
# SSH
username = 'admin'
password = 'Cisc0123'
from qyt_devnet.qyt_cmd import QYTHuaweiSSH
client1 = QYTHuaweiSSH(hostname=r1, username=username, password=password)
print(client1.dis_cur())
