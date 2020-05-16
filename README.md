# Project Title

乾颐堂 现任明教教主 网络设备自动化高级封装

## Getting Started

qyt_devnet是我做的一个简单的华为自动化项目, 可以直接pip install qyt_devnet使用, 如果大家觉得好我可以维护更新这个项目, 加入更多华为设备的支持! 其实非华为的设备用netmiko就好了! 由于华为不受人待见,大家都不支持, 只有自己搞一个了


## Authors

乾颐堂 现任明教教主 [YouTube](https://www.youtube.com/channel/UCsvHsD_g8j2IEZDlVzMC3Qw)

## 使用案例

>>> from qyt_devnet.qyt_snmp import QYTHuaweiSNMP
>>> r1 = '192.168.1.151'
>>> community_ro = "QytangR0"
>>> snmp_client = QYTHuaweiSNMP(r1, community_ro)
>>> print(snmp_client.sys_desc())

>>> username = 'admin'
>>> password = 'Cisc0123'
>>> from qyt_devnet.qyt_cmd import QYTHuaweiSSH
>>> client1 = QYTHuaweiSSH(hostname=r1, username=username, password=password)
>>> print(client1.dis_cur())
