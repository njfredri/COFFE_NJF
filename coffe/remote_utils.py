import subprocess
import os

class RemoteUtils:
    def run_cmd(cmd_str, username, remote_host, remote_password:str = None, remotedir:str = None):
        """
        runs command string in a remote bash shell
        """
        print("Command: %s" %(cmd_str))
        
        ssh_call = 'ssh ' + username + '@' + remote_host
        if remote_password != None:
            sshpass = 'sshpass -p' + "'" + remote_password + "'"
            ssh_call = sshpass + ' ' + ssh_call
        
        command = cmd_str
        
        if remotedir != None:
            command = 'cd ' + remotedir + '; ' + command
        
        print(ssh_call)
        sshcommand = ssh_call + " '" + command + "' "
        print(sshcommand)
        subprocess.call(sshcommand,shell=True,executable="/bin/bash")
    
    def run_cmds(cmds: list, username, remote_host, remote_password:str = None, remotedir:str = None):
        """
        runs command string in a remote bash shell
        """
        print("Command: %s" %(str(cmds)))
        
        ssh_call = 'ssh ' + username + '@' + remote_host
        if remote_password != None:
            sshpass = 'sshpass -p' + "'" + remote_password + "'"
            ssh_call = sshpass + ' ' + ssh_call
        
        command = ''
        
        for cmd in cmds:
            command = command + cmd + '; '
        
        if remotedir != None:
            command = 'cd ' + remotedir + '; ' + command
        
        print(ssh_call)
        sshcommand = ssh_call + " '" + command + "' "
        print(sshcommand)
        subprocess.call(sshcommand,shell=True,executable="/bin/bash")

    
    # def run_commands

    def copyFileToServer(file, remotedir, username, remote_host, remote_password:str = None):
        command = 'scp ' + file + ' ' + username + '@' + remote_host + ':' + remotedir
        if remote_password != None:
            command = 'sshpass -p ' + remote_host + ' ' + command
        subprocess.call(command,shell=True,executable="/bin/bash")

    def copyFileFromServer(filename, remotedir, localdir, username, remote_host, remote_password:str = None):
        remotepath = os.path.join(remotedir, filename)
        command = 'scp ' + username + '@' + remote_host + ':' + remotepath + ' ' + localdir
        if remote_password != None:
            command = 'sshpass -p ' + remote_host + ' ' + command
        subprocess.call(command,shell=True,executable="/bin/bash")
        
    def copyDirToServer(dir, remotedir, username, remote_host, remote_password:str = None):
        command = 'scp -r ' + dir + ' ' + username + '@' + remote_host + ':' + remotedir
        if remote_password != None:
            command = 'sshpass -p ' + remote_host + ' ' + command
        subprocess.call(command,shell=True,executable="/bin/bash")