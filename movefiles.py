#coding:UTF8
import time
import datetime
import os
import os.path
import shutil
import sys
def get_size(start_path = 'd:\\'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_filename(path):
    filepath = []
    for root, dirs, files in os.walk(path):
        if '$RECYCLE.BIN' not in root and 'System Volume Information' not in root:
            for name in files:
                filepath.append(root + '\\' + name)
    return filepath

def get_filemodtime(filename):
    ModifiedTime = time.localtime(os.stat(filename).st_mtime)  # 文件的修改时间
    y = time.strftime('%Y', ModifiedTime)
    m = time.strftime('%m', ModifiedTime)
    d = time.strftime('%d', ModifiedTime)
    H = time.strftime('%H', ModifiedTime)
    M = time.strftime('%M', ModifiedTime)
    modtime = datetime.datetime(int(y), int(m), int(d), int(H), int(M))
    return modtime

def get_filecreatetime(filename):
    CreateTime = time.localtime(os.stat(filename).st_ctime)  # 文件的修改时间
    y = time.strftime('%Y', CreateTime)
    m = time.strftime('%m', CreateTime)
    d = time.strftime('%d', CreateTime)
    H = time.strftime('%H', CreateTime)
    M = time.strftime('%M', CreateTime)
    createtime = datetime.datetime(int(y), int(m), int(d), int(H), int(M))
    return createtime

if __name__=='__main__':
	log_time=time.strftime("%Y%m%d%H%M%S", time.localtime())
	file_name='move_'+log_time+'.txt'
	log_file = open(file_name, 'w')
	sys.stdout = log_file
    nowtime = datetime.datetime.now()
    #path=raw_input('请输入要统计的文件夹:')
    #print path.split(':')[0].lower()
    upper_path=r'd:\JET7000E_SPC\1_R'
    dirs=os.listdir(upper_path)
    for dir in dirs:
        path=upper_path+'\\'+dir
        if os.path.isdir(path):
            #print (path)
            print ('Now analyze '+path)
            
            if os.path.exists(path) and path.split(':')[0].lower()!='c' :

                filename=get_filename(path)
            

                #print filename
                for i  in filename:
                    try:
                        modtime=get_filemodtime(i)
                        
                        timedelt=(nowtime - modtime ).days
                        if timedelt>14 and os.path.splitext(i)[1][1:].lower() not  in ['db','ini','pdf','prg','mdb','off']:
                            print (str(i) +' 已经'+str(timedelt)+'天未修改')
                            path1=os.path.split(i)
                            pathdir=path1[0]
                            destpath = 'O:\\' + pathdir[3:] + '\\'
                            destfile=destpath+path1[1]
                            if os.path.exists(destpath):
                                pass
                            else:
                                os.makedirs(destpath)
                            #print destfile
                            #print pathdir
                            #os.rename(i,destfile)
                            shutil.move(i,destfile)
                    except Exception as e:
                        print (e)
                #print destpath
            else:
                print ('请输入正确的路径')
    log_file.close()
