class BaseResponse(object):     #ret不适用字典形式，改为封装成对象形式，以后要添加值，继承它即可
    def __init__(self):
        self.status = True
        self.data = None
        self.error = None