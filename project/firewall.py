#coding:utf8
import commands
from system.config import conf
class firewall():
    white_ip=set()
    forbid_ip=set()
    def __init__(self):
        self.white_ip=conf.read("white_ip.json")


    def  check(self,data):
        for value in data["ip_list"]:
            ip = value[1].split(":")[0]
            # if ((data["int"]>200 or data["out"]>200)  and len(self.forbid_ip)<3) or int(value[0])>15:
            if int(value[0])>15:
                if ip not in self.white_ip and ip not in self.forbid_ip:
                    self.forbid_ip.add(ip)
                    self.drop_ip(ip)

            else:
                break
        return self.forbid_ip

    def drop_ip(self,ip):
        cmd="iptables -A INPUT -s "+ip+" -j DROP"
        result=commands.getstatusoutput(cmd)
        print result
