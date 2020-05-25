from qyt_devnet.modules.snmp_v2_get import snmpv2_get
from qyt_devnet.modules.snmp_v2_getnext import snmpv2_getnext


class QYTHuaweiSNMP:
    def __init__(self, ip, ro, port=161):
        self.ip = ip
        self.ro = ro
        self.port = port

    def sys_desc(self):
        return snmpv2_get(self.ip, self.ro, "1.3.6.1.2.1.1.1.0", port=self.port)[1]

    def hostname(self):
        return snmpv2_get(self.ip, self.ro, "1.3.6.1.2.1.1.5.0", port=self.port)[1]

    def location(self):
        return snmpv2_get(self.ip, self.ro, "1.3.6.1.2.1.1.6.0", port=self.port)[1]

    def cpu_usage(self):
        return int(snmpv2_get(self.ip, self.ro, "1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.67108873", port=self.port)[1])

    def mem_usage(self):
        return int(snmpv2_get(self.ip, self.ro, "1.3.6.1.4.1.2011.5.25.31.1.1.1.1.7.67108873", port=self.port)[1])

    def get_ifs(self):
        return [if_name[1] for if_name in snmpv2_getnext(self.ip, self.ro, "1.3.6.1.2.1.2.2.1.2", port=161)]

    def get_if_speed(self):
        return [[name, speed] for name, speed in zip(self.get_ifs(), [if_speed[1] for if_speed in snmpv2_getnext(self.ip, self.ro, "1.3.6.1.2.1.2.2.1.5", port=161)])]

    def get_if_in_bytes(self):
        return [[name, speed] for name, speed in zip(self.get_ifs(), [if_speed[1] for if_speed in snmpv2_getnext(self.ip, self.ro, "1.3.6.1.2.1.2.2.1.10", port=161)])]

    def get_if_out_bytes(self):
        return [[name, speed] for name, speed in zip(self.get_ifs(), [if_speed[1] for if_speed in snmpv2_getnext(self.ip, self.ro, "1.3.6.1.2.1.2.2.1.16", port=161)])]


if __name__ == '__main__':
    r1 = '192.168.1.151'
    community_ro = "QytangR0"
    snmp_client = QYTHuaweiSNMP(r1, community_ro)
    # 系统描述
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
