class BasePlugin(object):   #1.约束 2.公共方法
    def __init__(self,host=None):   #构造方法
        self.hostname = host
    def execute(self):      #判断是否是Linux
        return self.linux()
    def linux(self):    #约束
        raise NotImplementedError('插件必须实现Linux方法')
    def windows(self):
        raise NotImplementedError('插件必须实现windows方法')
    def agent_cmd(self,cmd):    #公共方法,本地执行命令,agent模式
        import subprocess
        v = subprocess.getoutput(cmd)
        return v

    def ssh_cmd(self,cmd):      #ssh模式，远程执行
        import paramiko
        private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')       # 创建SSH对象
        ssh = paramiko.SSHClient()      # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())       # 连接服务器
        ssh.connect(hostname=self.hostname, port=22, username='wupeiqi', key=private_key)       # 执行命令,hostname调用上面的构造方法
        stdin, stdout, stderr = ssh.exec_command(cmd)      # 获取命令结果，
        result = stdout.read()      # 关闭连接
        ssh.close()
        return result

    def salt_cmd(self,cmd):     #slat模式
        #方式一
        # import subprocess
        # v = subprocess.getoutput('salt %s cmd.run %s' %(self.hostname,cmd))     #使用subprocess
        # return v
        #方式二
        import slat.client      #跟上方法差不多，要先下载slat模块
        local = salt.client.LocalClient()
        result = local.cmd(self.hostname, 'cmd.run', [cmd])
        return result

    def cmd(self,c):          #判断模式，通过配置文件判断
        from config import settings
        if settings.MODE == "Agent":    # 判断agent模式执行
            result = self.agent_cmd(c)
        elif settings.MODE == "SSh":    #判断ssh模式执行
            result = self.ssh_cmd(c)
        elif settings.MODE == "Salt":   #判断salt模式执行
            result = self.salt_cmd(c)
        else:
            raise Exception('配置文件中Mode设置错误')
        return result

# obj = BasePlugin()
# obj.execute()
#执行上面的会直接报异常

class DiskPlugin(BasePlugin):   #继承BasePlugin
    def linux(self):    #用于执行命令，获取资产信息
        # return "disk"
        result =  self.cmd("df -Th")
        return result
    def windows(self):
        return "disk"

class MemPlugin(BasePlugin):
    def linux(self):
        # return "Mem"
        result = self.shell_cmd('free -m')
        return result

class NicPlugin(BasePlugin):
    def linux(self):
        result = self.cmd('ifconfig')
        #使用正则，字符串操作
        return  result

obj = DiskPlugin()
r = obj.execute()
print(r)        #r输出为disk，执行顺序为：1.execute 2.return self.linux() 3.下面的def linux(self): 4.return "disk"

obj = NicPlugin()
result = obj.execute()      #获取网卡信息