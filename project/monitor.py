#!/usr/bin/env Python
import time
import sys
import commands
import redis
import json
from project.firewall import firewall
from RedisModel.SystemRedis import system_redis


class Flow():
    STATS = []
    redis_server = object()
    fire = object()

    def __init__(self):
        self.INTERFACE = 'eth0'
        self.fire = firewall()
        self.rx()
        self.tx()

    def rx(self):
        ifstat = open('/proc/net/dev').readlines()
        for interface in ifstat:
            if self.INTERFACE in interface:
                stat = float(interface.split()[1])
                self.STATS[0:] = [stat]

    def tx(self):
        ifstat = open('/proc/net/dev').readlines()
        for interface in ifstat:
            if self.INTERFACE in interface:
                stat = float(interface.split()[9])
                self.STATS[1:] = [stat]

    def recount(self):
        data = dict()
        last_stats = list(self.STATS)
        self.rx()
        self.tx()
        RX_RATE = round((self.STATS[0] - last_stats[0]), 3)
        TX_RATE = round((self.STATS[1] - last_stats[1]), 3)
        RX_RATE=self.transform_byte(RX_RATE)
        TX_RATE=self.transform_byte(TX_RATE)
        data["int"] = RX_RATE
        data["out"] = TX_RATE
        data["ip_list"] = self.ip()
        data["drop_ip"] = list(self.fire.check(data))
        system_redis.add(data)

    def ip(self):
        ip_data = list()
        command_str = """netstat -ntu | awk '{print $5}'  | sort | uniq -c | sort -nr|grep -v '127.0.0\|Address\|servers'"""
        count_list = commands.getstatusoutput(command_str)[1].split("\n")
        for value in count_list:
            ip_data.append(value.strip().split(" "))
        return ip_data

    def transform_byte(self, data):
        if data > 1024 * 1024:
            data = str(round(data / (1024 * 1024), 3)) + "Mb"
        elif data > 1024:
            data = str(round(data / (1024), 3)) + "Kb"
        else:
            data = str(data) + "b"
        return data



