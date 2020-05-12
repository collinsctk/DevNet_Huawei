import paramiko
from paramiko_expect import SSHClientInteraction


class QYTHuaweiSSH:
    def __init__(self, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=hostname, username=username, password=password)

    def dis_cur(self, verbose=False):
        try:
            with SSHClientInteraction(self.client, timeout=20, display=verbose) as interact:
                interact.expect('<[\S\s]+>')
                screen_change_cmds = ['system-view', 'user-interface vty 0 4', 'screen-length 0']
                for cmd in screen_change_cmds:
                    interact.send(cmd)
                    interact.expect('\[[\S\s]+\]')
                interact.send('return')
                interact.expect('<[\S\s]+>')

                interact.send('display current-configuration')
                interact.expect('return', timeout=5)
                cmd_output = interact.current_output_clean
                return cmd_output
        except Exception as e:
            print(e)
        finally:
            self.client.close()

    def display(self, display_cmds, verbose=False):
        try:
            return_result_list = []
            with SSHClientInteraction(self.client, timeout=20, display=verbose) as interact:
                interact.expect('<[\S\s]+>')
                screen_change_cmds = ['system-view', 'user-interface vty 0 4', 'screen-length 0']
                for cmd in screen_change_cmds:
                    interact.send(cmd)
                    interact.expect('\[[\S\s]+\]')
                interact.send('return')
                interact.expect('<[\S\s]+>')
                for cmd in display_cmds:
                    interact.send(cmd)
                    interact.expect('<[\S\s]+>')
                    cmd_output = interact.current_output_clean
                    return_result_list.append(cmd_output)
            return return_result_list
        except Exception as e:
            print(e)
        finally:
            self.client.close()

    def config(self, config_cmds, verbose=True):
        try:
            config_cmds.insert(0, 'system-view')
            with SSHClientInteraction(self.client, timeout=20, display=verbose) as interact:
                interact.expect('<[\S\s]+>')
                for cmd in config_cmds:
                    interact.send(cmd)
                    interact.expect('\[[\S\s]+\]')
        except Exception as e:
            print(e)
        finally:
            self.client.close()


if __name__ == '__main__':
    r1 = '192.168.1.151'
    r2 = '192.168.1.152'
    username = 'admin'
    password = 'Cisc0123'
    client1 = QYTHuaweiSSH(hostname=r1, username=username, password=password)
    client2 = QYTHuaweiSSH(hostname=r2, username=username, password=password)

    # 查看Current Config
    print(client1.dis_cur())

    # 配置OSPF
    c_cmds_1 = ['sysname AR1',
                'interface LoopBack 0',
                'ip address 1.1.1.1 32',
                'interface GigabitEthernet 0/0/2',
                'ip address 10.1.1.1 24',
                'ospf 1 router-id 1.1.1.1',
                'area 0.0.0.0',
                'network 10.1.1.0 0.0.0.255',
                'network 1.1.1.1 0.0.0.0'
                ]

    c_cmds_2 = ['sysname AR2',
                'interface LoopBack 0',
                'ip address 2.2.2.2 32',
                'interface GigabitEthernet 0/0/2',
                'ip address 10.1.1.2 24',
                'ospf 1 router-id 2.2.2.2',
                'area 0.0.0.0',
                'network 10.1.1.0 0.0.0.255',
                'network 2.2.2.2 0.0.0.0'
                ]
    client1.config(c_cmds_1, verbose=True)
    client2.config(c_cmds_2, verbose=True)

    snmp_cmds = ['snmp-agent sys-info version v2c',
                 'snmp-agent sys-info contact collinsctk',
                 'snmp-agent sys-info location beijing_qyt',
                 'snmp-agent community read QytangR0'
                 ]

    client1.config(snmp_cmds.copy(), verbose=True)
    client2.config(snmp_cmds.copy(), verbose=True)

    # # 其他查看内容
    for r in client1.display(['display ospf peer', 'dis ver']):
        print(r)
