# -*- coding: utf-8 -*-
# @Author  : Louzhichen
import os,os.path,shutil,msvcrt
audio,video,compressedFile,photo,program,documents,web,pythonFile,torrent,ISOfile,ebook,androidfile=['.mp3','.wma','.flac'],['.mp4','.avi','.mov','.mpeg','.ts','.flv','.m4v','.mkv','.m3u8'],['.7z','.zip','.rar','.cab','.jar','.lzh'],['.jpg','.jpeg','.png','.gif','.bmp','.jfif'],['.exe','.com','bat','.msi'],['.doc','.docx','.xls','.xlsx','.csv','.ppt','.pptx','.pdf','.txt'],['.html','.htm'],['.py'],['.torrent'],['.iso'],['.epub','.mobi'],['.apk']
fileExtName=[audio,video,compressedFile,photo,program,documents,web,pythonFile,torrent,ISOfile,ebook,androidfile]
fileExtName2=["Music","Video","Compressed","Photo","Program","Document","Web","Python","Torrent","ISO","Book","Android"]
inputpath = input("请输入路径，按回车键运行")
def moveMyFile(newpath):
    if not os.path.exists(f"{inputpath}/{newpath}"):
        os.makedirs(f"{inputpath}/{newpath}")
    try:
        shutil.move(f"{inputpath}/{i}", f"{inputpath}/{newpath}")
        print(f"成功移动{inputpath}\{i}")
    except Exception:
        print(f"未能移动{inputpath}\{i}")
for i in os.listdir(inputpath):
    if os.path.isfile(f"{inputpath}/{i}"):
        extName=os.path.splitext(f"{inputpath}/{i}")[-1]
        for j in range(len(fileExtName)):
            if extName in fileExtName[j]:
                moveMyFile(fileExtName2[j])
            j=j+1
print("请按任意键退出")
ord(msvcrt.getch())