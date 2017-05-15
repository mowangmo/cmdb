from . base import BasePlugin
from lib.response import BaseResponse
import traceback


class NicPlugin(BasePlugin):
    def linux(self):
        ret = BaseResponse()
        try:
            result = self.cmd("nic")
            # ret['data'] = result
            ret.data = result
        except Exception as e:
            # ret['status'] = False
            # ret['error'] = traceback.format_exc()       #traceback让日志显示的更详细
            ret.status = False
            ret.error = traceback.format_exc()
        return ret