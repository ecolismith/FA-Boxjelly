print("hello world")
import time
import subprocess
from subprocess import Popen, PIPE
cameraIP = "169.254.15.202"
cmdPing = 'ping -c 1 {} | grep "bytes from"'.format(cameraIP)




TIME_OUT = 15
TIME_WAIT = 5

# uses ping to check if camera ethernet is connected
def ping_camera():
    try:
        res = subprocess.check_output(cmdPing, shell=True)
        if res:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def jpg_download(pic_id,pic_name, target_path):
    sftp_cmd = "sshpass -p 3vlig sftp -oStrictHostKeyChecking=no fliruser@" + cameraIP + ":/FLIR/images/img_20000104_084044_600.{fmt} {name}.{fmtN}"
    try:
        full_name = "{}cap{:04d}_{}".format(target_path, pic_id, pic_name)
        cmd = subprocess.call(bytes(sftp_cmd.format(fmt="jpg", name=full_name, fmtN="jpg"),encoding='utf-8'), shell=True)
        print("download successful")
    except Exception as e:
        print("[SFTP] Download Error: {}".format(e))
        result = False

def time_out_error(popen, error_message):
    timer = time.time()
    while not popen.stdout.read(1):
        time.sleep(TIME_WAIT)
        if time.time > timer + TIME_OUT:
            popen.kill()
            print(error_message)
        return True
    return False

def send_command(cmd_str,success_message,print_lines):
    ssh_cmd = "sshpass -p 3vlig ssh -oStrictHostKeyChecking=no -t -t fliruser@{}".format(cameraIP)
    # open interactive session to camera
    try:
        popen = Popen(ssh_cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        # check for a response
        if not popen.stdout.read(1):
            popen.kill()
            print("popen error: no command input")
            return False,[]
        popen.stdout.flush()
        print("popen session set up")
        # send command to camera
        popen.stdin.write(bytes("{}\n".format(cmd_str), encoding='utf-8'))
        popen.stdin.flush()
        print("popen command sent")
        if time_out_error(popen,"ERROR, time out: no response from device"):
            return False,[]
        
        # read two lines
        result = []
        for i in range(0,print_lines):
            result = result + popen.stdout.readline().split()
        #result = popen.stdout.readline()
        print("popen result received")
        #end popen session
        popen.stdin.write(bytes("exit\n", encoding='utf-8'))
        popen.stdin.flush()
        if time_out_error(popen,"ERROR, time out: when exit"):
            return False,[]
        print(success_message)
        return True, result

    except Exception as e:
        print("[SSH ERROR] {}".format(e))
    return False, []

def camera_ssh_trigger_single(file_name):
    sshCamCapJPG = "/FLIR/usr/bin/store -j /FLIR/images/temp.rjpg"
    ssh_cmd_capjpg = "/FLIR/usr/bin/store -v /FLIR/images/" + file_name + ".jpg"
    success_message = "capture successful"
    flag, result = send_command(sshCamCapJPG,success_message,2)
    if flag:
        print(result)

# gets camera version info over SSH
def camera_ssh_version():
    ssh_cmd_version = "/FLIR/usr/bin/version"
    success_message = "ssh version got"
    flag, result = send_command(ssh_cmd_version,success_message,2)
    if flag:
        print(result)


if __name__ == '__main__':
    res = ping_camera()
    if res:
        print("[PWR] [FLIR] Camera detected, Wait for camera OS boot")
    camera_ssh_version()
    camera_ssh_trigger_single("test.jpg")
    jpg_download(11,"02","./static/")
