from . base import BasePlugin
import traceback
from lib.response import BaseResponse


class DiskPlugin(BasePlugin):   #继承BasePlugin
    def linux(self):    #用于执行命令，获取资产信息
        # return "disk"
        # ret = {'status':True,'data':None,'error':None}  #为异常处理设置一个字典,但是这么做不好，要每个插件都写一遍
        ret = BaseResponse()
        try:
            result =  self.cmd("df -Th")
            # ret['data'] = result
            ret.data = result
        except Exception as e:
            # ret['status'] = False
            # ret['error'] = traceback.format_exc()       #traceback让日志显示的更详细
            ret.status = False
            ret.error = traceback.format_exc()
            #写入本地日志
        return ret