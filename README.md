# 主题

乾颐堂 现任明教教主 网络设备自动化高级封装

## 项目描述

qyt_devnet是我做的一个简单的华为自动化项目, 可以直接pip install qyt_devnet使用, 如果大家觉得好我可以维护更新这个项目, 加入更多华为设备的支持! 其实非华为的设备用netmiko就好了! 由于华为不受人待见,大家都不支持, 只有自己搞一个了


## 作者

乾颐堂 现任明教教主 [YouTube首页](https://www.youtube.com/channel/UCsvHsD_g8j2IEZDlVzMC3Qw)

## 使用案例

\# SNMP<br>
from qyt_devnet.qyt_snmp import QYTHuaweiSNMP<br>
r1 = '192.168.1.151'<br>
community_ro = "QytangR0"<br>
snmp_client = QYTHuaweiSNMP(r1, community_ro)<br>
\# 系统描述<br>
print(snmp_client.sys_desc())<br>
\# 主机名<br>
print(snmp_client.hostname())<br>
\# 地点<br>
print(snmp_client.location())<br>
\# CPU利用率<br>
print(snmp_client.cpu_usage())<br>
\# 内存利用率<br>
\print(snmp_client.mem_usage())<br>
\# 接口清单<br>
\print(snmp_client.get_ifs())<br>
\# 接口速率<br>
print(snmp_client.get_if_speed())<br>
\# 接口入向字节数<br>
print(snmp_client.get_if_in_bytes())<br>
\# 接口出向字节数<br>
print(snmp_client.get_if_out_bytes())<br>
<br>
\# SSH<br>
username = 'admin'<br>
password = 'Cisc0123'<br>
from qyt_devnet.qyt_cmd import QYTHuaweiSSH<br>
client1 = QYTHuaweiSSH(hostname=r1, username=username, password=password)<br>
print(client1.dis_cur())<br>
