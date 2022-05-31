import http
import os
from re import S
import sys
import platform
import requests


def print_help():
    help_text = """
help document-对应参数：
info-get information
ip-get ip
name-write a name to file
run-run some Linux command
"""
    print(help_text)

def print_ip():
    #print(platform.machine())
    #test platform

    #获取ip地址
    ip = requests.get("http://ipinfo.io/ip")
    #没加.text的时候，打印了<Response [200]>
    print(ip.text)
    exit()


def main():
    if(len(sys.argv) == 1):
        print_help()
        exit()

    if(sys.argv[1]=="ip"):
        print_ip()
        

    if(sys.argv[1]=="run"):
        #执行查看当前目录的命令
        cmd = sys.argv[2]
        if(cmd == "ls"):
        #使用OS模块来执行bash命令
        #os.system(命令)  在shell中执行命令
            #os.system("ls") 
            #在windows中os.system用ls会报错：不是内部或外部命令，也不是可运行的程序，或批处理文件。
            #原因是windows没有ls这个命令
            os.system("dir")

        else:
            print("command not found")
            exit()
            #要退出进程
        pass


    if(sys.argv[1]=="name"):
        name = input("Please input your name:")
        print(name)
        exit()


if __name__ == "__main__":
    main()

#直接执行python脚本，__name__就是__main__
#模块import的情况下这个值就不会是__main__