#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

# fulfill the functions of command on Cisco devices

import time
import paramiko


class QYTCiscoSSH:
    def __init__(self, hostname, username, password):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=hostname, username=username, password=password)

    def show_run(self):
        try:
            stdin, stdout, stderr = self.client.exec_command('show running-config')
            return stdout.read().decode()
        except Exception as e:
            print(e)
        finally:
            self.client.close()

    def show(self, show_cmds):
        return_result_list = []
        try:
            remote = self.client.invoke_shell()
            remote.send('term len 0\n')
            time.sleep(1)
            for cmd in show_cmds:
                remote.send('%s \n' % cmd)
                time.sleep(2)
                buf = remote.recv(65000)
                f = open('sshlogfile0001.txt', 'ab')
                f.write(buf)
                f.close()
                return_result_list.append(buf)
            return return_result_list
        except Exception as e:
            print(e)
        finally:
            self.client.close()

    def config(self, config_cmds):
        try:
            enable = 'Cisc0123'
            wait_time = 2
            verbose = True
            chan = self.client.invoke_shell()
            chan.send('term len 0\n')
            time.sleep(1)
            login_mode = chan.recv(2048).decode()
            if '>' in login_mode:
                chan.send("enable\n".encode())
                time.sleep(1)
                en_password = enable + '\n'
                chan.send(en_password)
            for cmd in config_cmds:
                chan.send(b'\n')
                chan.send(cmd.encode())
                chan.send(b'\n')
                x = chan.recv(2048).decode()
                if verbose:
                    print(x)
                time.sleep(wait_time)
        except Exception as e:
            print(e)
        finally:
            self.client.close()


if __name__ == '__main__':
    r1 = '192.168.200.101'
    username = 'admin'
    password = 'Cisc0123'
    client1 = QYTCiscoSSH(hostname=r1, username=username, password=password)
    # print(client1.show_run())
    cmds = ['show ver', 'show ip int br', 'end']
    # print(client1.show(cmds))
    client1.config(cmds)
