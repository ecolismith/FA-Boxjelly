import time
import subprocess
from subprocess import Popen, PIPE
camera_IP = "169.254.15.202"

TIME_OUT = 15
TIME_WAIT = 5

# uses ping to check if camera ethernet is connected
def ping_camera():
    cmdPing = 'ping -c 1 {} | grep "bytes from"'.format(camera_IP)
    try:
        res = subprocess.check_output(cmdPing, shell=True)
        if res:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# download a jpg file from the camera ethernet website
# pic_id is the id of the picture
# pic name is the name of the picture, you have to know id and the name of the picture to download that.
def jpg_download(pic_id,pic_name, target_path):
    sftp_cmd = "sshpass -p 3vlig sftp -oStrictHostKeyChecking=no fliruser@" + camera_IP + ":/FLIR/images/"+ pic_name +".{fmt} {name}.{fmtN}"
    try:
        full_name = "{}cap{:04d}_{}".format(target_path, pic_id, pic_name)
        cmd = subprocess.call(bytes(sftp_cmd.format(fmt="jpg", name=full_name, fmtN="jpg"),encoding='utf-8'), shell=True)
        print("download successful")
    except Exception as e:
        print("[SFTP] Download Error: {}".format(e))
        result = False

# this is used for report when time out 
# popen is the sesstion we currently used
# error_message is the message to print when time out.
def time_out_error(popen, error_message):
    timer = time.time()
    while not popen.stdout.read(1):
        time.sleep(TIME_WAIT)
        if time.time > timer + TIME_OUT:
            popen.kill()
            print(error_message)
        return True
    return False

# this function sends a command to the cameara through popen. 
# cmd string is the command to send
# success_message is the information to print when request successful
# print lines is the number of lines to print when feedback received
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
        # read lines
        result = []
        for i in range(0,print_lines):
            result = result + popen.stdout.readline().split()
            
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

# this functin used popen to send a command to the cameara to take a picture
# the file_name is the name of the picture to be downloaded, 
# pic id is hard-coded with 2, we are not gonna use it. 
def camera_ssh_trigger_single(file_name):
    ssh_cmd_capjpg = "/FLIR/usr/bin/store -v /FLIR/images/" + file_name + ".jpg"
    success_message = "capture successful"
    flag, result = send_command(ssh_cmd_capjpg,success_message,2)
    if flag:
        print(result)

# gets camera version info over SSH
def camera_ssh_version():
    ssh_cmd_version = "/FLIR/usr/bin/version"
    success_message = "ssh version got"
    flag, result = send_command(ssh_cmd_version,success_message,2)
    if flag:
        print(result)

# the main function first ping the camera to check the status
# and then the capture and downloa the picture to the hard-coded path.
if __name__ == '__main__':
    res = ping_camera()
    if res:
        print("[PWR] [FLIR] Camera detected, Wait for camera OS boot")
        camera_ssh_version()
        camera_ssh_trigger_single("test.jpg")
        jpg_download(11,"01","/home/dikaiz/Downloads/")
