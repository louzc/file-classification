import os
import shutil
import os.path
import time
audio,video,compressedfiles,photo,program,officeword,officeexcle,officeppt,pdf,txt,web,pythonfile,torrent,ISOfile,ebook=['.mp3','.wma','.flac'],['.mp4','.avi','.mov','.mpeg','.ts','.flv','.m4v','.mkv','.m3u8'],['.7z','.zip','.rar','.cab','.jar','.lzh'],['.jpg','.jpeg','.png','.gif','.bmp','.jfif'],['.exe','.com','bat','.msi'],['.doc','.docx'],['.xls','.xlsx','.csv'],['.ppt','.pptx'],['.pdf'],['.txt'],['.html','.htm'],['.py'],['.torrent'],['.iso'],['.epub','.mobi']
documentfiles=officeexcle+officeppt+officeword+txt+pdf
def movefile(newpath):
    if not os.path.exists(path+"/"+newpath):
        os.makedirs(path+"/"+newpath)
    shutil.move(path+"/"+i,path+"/"+newpath)
def del_emp_dir(path):           #删除空文件夹
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)  #os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
                #print(dir)
            except Exception as e:
                pass
def OpenDir():
    os.system('explorer '+path) #注意空格！
    return
path_input=input(r"请输入路径，按回车键运行/input a link")
path=path_input
start = time.perf_counter()
list=os.listdir(path)
for i in list:
    if os.path.isfile(path+"/"+i):
        ext_name=os.path.splitext(i)[-1]
        #print(ext_name)
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
        else:
            pass
    if os.path.isdir(path+"/"+i):
            del_emp_dir(path)
print("All operates have been successfully done.")
end= time.perf_counter()
runningtime=end-start
intrunningtime=str(int(1000*runningtime)/1000)
print('操作路径：'+path)
print('本程序运行时间：'+intrunningtime+'秒')