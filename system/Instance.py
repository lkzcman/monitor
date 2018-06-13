class Instance(object):
    @classmethod
    def call_method(cls,module_name,class_name,method,data):
        if not hasattr(cls,class_name ):
            obj =cls.createInstance(module_name, class_name)
            setattr(cls, class_name, obj)
        obj=getattr(cls,class_name)
        return getattr(obj,method)(data)

    @classmethod
    def createInstance(cls,module_name, class_name, *args, **kwargs):
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        obj = class_meta(*args, **kwargs)
        return obj
