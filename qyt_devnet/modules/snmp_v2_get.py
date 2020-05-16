#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


from pysnmp.hlapi import *


def snmpv2_get(ip, community, oid, port=161):
    # varBinds是列表，列表中的每个元素的类型是ObjectType（该类型的对象表示MIB variable）
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),  # 配置community
               UdpTransportTarget((ip, port)),  # 配置目的地址和端口号
               ContextData(),
               ObjectType(ObjectIdentity(oid))  # 读取的OID
               )
    )
    # 错误处理
    if error_indication:
        print(error_indication)
    elif error_status:
        print('%s at %s' % (
            error_status,
            error_index and var_binds[int(error_index) - 1][0] or '?'
        )
              )
    # 如果返回结果有多行,需要拼接后返回
    result = ""

    for varBind in var_binds:

        result = result + varBind.prettyPrint() # 返回结果！
    # 返回的为一个元组,OID与字符串结果
    # print(result)
    return result.split("=")[0].strip(), result.split("=")[1].strip()


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 系统描述
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.2.1.1.1.0", port=161))
    # 联系人
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.2.1.1.4.0", port=161))
    # 主机名
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.2.1.1.5.0", port=161))
    # 地点
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.2.1.1.6.0", port=161))
    # CPU利用率
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5.67108873", port=161))
    # 内存利用率
    print(snmpv2_get("192.168.1.151", "QytangR0", "1.3.6.1.4.1.2011.5.25.31.1.1.1.1.7.67108873", port=161))


