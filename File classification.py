# -*- coding: utf-8 -*-
# @Author  : Louzhichen
# 比较混乱，随便看看就好。
# 注意：没有验证要分类的文件与目标文件夹下的文件重名得情况，会报错，请自行修改。
# 注意：如果文件夹过大，本程序运行速度会比较慢。测试过程中，50G的文件夹全部操作完成大概需要两分钟。
import contextlib,os,os.path,time,shutil
audio,video,compressedfiles,photo,program,officeword,officeexcle,officeppt,pdf,txt,web,pythonfile,torrent,ISOfile,ebook,androidfiles=['.mp3','.wma','.flac'],['.mp4','.avi','.mov','.mpeg','.ts','.flv','.m4v','.mkv','.m3u8'],['.7z','.zip','.rar','.cab','.jar','.lzh'],['.jpg','.jpeg','.png','.gif','.bmp','.jfif'],['.exe','.com','bat','.msi'],['.doc','.docx'],['.xls','.xlsx','.csv'],['.ppt','.pptx'],['.pdf'],['.txt'],['.html','.htm'],['.py'],['.torrent'],['.iso'],['.epub','.mobi'],['.apk']
documentfiles = officeexcle+officeppt+officeword+txt+pdf
path = input("请输入路径，按回车键运行")
if not path:
    path=r"C:\Users\louzh\下载"
def movefile(newpath):
    if not os.path.exists(f"{path}/{newpath}"):
        os.makedirs(f"{path}/{newpath}")
    shutil.move(f"{path}/{i}", f"{path}/{newpath}")
def del_dir(path):           #这个函数写得不好烂，应该可以优化，或者import一些库来解决
    for (root, dir, files) in os.walk(path):
        for item in dir:
            dir1 = os.path.join(root, item)
            with contextlib.suppress(Exception):         #消除报错，比try方便，有时间学习。
                os.rmdir(dir1)                  #删除文件夹，如果文件夹非空，抛出OSError。
st = time.perf_counter()
print(f'操作路径：{path}')
for i in os.listdir(path):
    if os.path.isfile(f"{path}/{i}"):
        ext_name=os.path.splitext(i)[-1]
        if ext_name in audio:
            movefile('Music')
        elif ext_name in documentfiles:
            movefile('Documents')
        elif ext_name in compressedfiles:
            movefile('Compressed')
        elif ext_name in photo:
            movefile('Photos')
        elif ext_name in video:
            movefile('Videos')
        elif ext_name in program:
            movefile('Programs')
        elif ext_name in web:
            movefile('Webpages')
        elif ext_name in pythonfile:
            movefile('Python')
        elif ext_name in torrent:
            movefile('Torrent')
        elif ext_name in ISOfile:
            movefile('光盘映像')
        elif ext_name in ebook:
            movefile('Books')
        elif ext_name in androidfiles:
            movefile('Apks')
    if os.path.isdir(f"{path}/{i}"):
        del_dir(path)
print("执行完成")
ed = time.perf_counter()
runningtime = str(int(1000*ed-st)/1000)
print(f'本程序运行时间：{runningtime}秒')