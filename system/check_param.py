# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from singleton import singleton
from system.config import conf
from system.Instance import Instance


@singleton
class check_param():
    def __init__(self):
        param_conf = conf.read("param.json")
        if not param_conf:
            param_conf = {}
        self.param_conf = param_conf

    def check_param(self, param, dict_data):
        for value in param:
            if value in self.param_conf.keys():
                if "require" in self.param_conf[value].keys():
                    if value not in dict_data:
                        return [1, "请填写" + value + "值"]
                    else:
                        if "value_list" in self.param_conf[value].keys():
                            if dict_data[value] not in self.param_conf[value]["value_list"]:
                                return [1, "请填写" + value + "有效值"]

                if "default_value" in self.param_conf[value].keys():
                    if value not in dict_data.keys:
                        dict_data[value] = self.param_conf[value]["default_value"]

                if "method" in self.param_conf[value].keys():
                    data = Instance.call_method(self.param_conf[value]["module_name"],
                                                self.param_conf[value]["class_name"], self.param_conf[value]["method"],
                                                dict_data[value])
                    dict_data[value] = data

            if value not in dict_data.keys() or not dict_data[value]:
                return [1, value + "值错误"]
        return [0, dict_data]


check = check_param()
