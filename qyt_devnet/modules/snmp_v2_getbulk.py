#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpv2_getbulk(ip, community, oid, count=25, port=161):
    cmd_gen = cmdgen.CommandGenerator()

    error_indication, error_status, error_index, var_bind_table = cmd_gen.bulkCmd(
        cmdgen.CommunityData(community),  # 配置community
        cmdgen.UdpTransportTarget((ip, port)),  # 配置IP地址和端口号
        0, count,  # 0为non-repeaters 和  25为max-repetitions(一个数据包中最多25个条目，和显示无关)
        oid,  # OID
    )

    """
    non-repeaters介绍
    the number of objects that are only expected to return a single GETNEXT instance, not multiple instances. Managers \
    frequently request the value of sysUpTime and only want that instance plus a list of other objects.
    max-repetitions介绍
    the number of objects that should be returned for all the repeating OIDs. Agent's must truncate the list to \
    something shorter if it won't fit within the max-message size supported by the command generator or the agent.
    详细介绍
    https://www.webnms.com/snmp/help/snmpapi/snmpv3/snmp_operations/snmp_getbulk.html
    """
    # 错误处理
    if error_indication:
        print(error_indication)
    elif error_status:
        print(error_status)

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for var_bind_table_row in var_bind_table:
        for item in var_bind_table_row:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 虽然count=25,但是脚本会自动过滤只显示主ID内的内容
    print(snmpv2_getbulk("192.168.1.151", "QytangR0", "1.3.6.1.2.1.2.2.1.2", count=25, port=161))
    for x, y in snmpv2_getbulk("192.168.1.151", "QytangR0", "1.3.6.1.2.1.2.2.1.2", count=25, port=161):
        print(x, y)
    # 接口速率
    print(snmpv2_getbulk("192.168.1.151", "QytangR0", "1.3.6.1.2.1.2.2.1.5", port=161))

    # 进接口字节数
    print(snmpv2_getbulk("192.168.1.151", "QytangR0", "1.3.6.1.2.1.2.2.1.10", port=161))

    # 出接口字节数
    print(snmpv2_getbulk("192.168.1.151", "QytangR0", "1.3.6.1.2.1.2.2.1.16", port=161))
