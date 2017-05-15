from src.plugins import nic
from src.plugins import disk

def func(hostname):
    nic_obj = nic.NicPlugin()       #linux方法，返回BaseResponse对象
    nic_info = nic_obj.execute()    #拿网卡信息

    disk_obj = disk.DiskPlugin()
    disk_info = disk_obj.execute()      #拿硬盘信息

    ret = {         #将信息写为一个字典，方便调用
        "nic":nic_info.__dict__,    #将对象转换为字典
        "dick":disk_info.__dict__,
    }
    return ret

if __name__=='__main__':
    from config import settings
    if settings.MODE == 'Agent':
        print('agnet')
        v = func(None)      #agent模式
        print(v)
    else:
        print('no agent')
        v = func('c1.com')      #ssh/salt 调用
        print(v)