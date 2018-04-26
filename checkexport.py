#coding:UTF8
import time
import datetime
import os
import os.path

def get_size(start_path = 'd:\\'): #获取文件夹大小,未使用到
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_filename(path): #获取路径下全部文件的名称
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
    CreateTime = time.localtime(os.stat(filename).st_ctime)  # 文件的创建时间
    y = time.strftime('%Y', CreateTime)
    m = time.strftime('%m', CreateTime)
    d = time.strftime('%d', CreateTime)
    H = time.strftime('%H', CreateTime)
    M = time.strftime('%M', CreateTime)
    createtime = datetime.datetime(int(y), int(m), int(d), int(H), int(M))
    return createtime

if __name__=='__main__':
    nowtime = datetime.datetime.now()
    #path=raw_input('请输入要统计的文件夹:')
    #print path.split(':')[0].lower()
    nums = [ '01']
    for aoi in nums:
        upper_path=r'e:\export'
        #print (upper_path)

        dirs=os.listdir(upper_path) #获取子目录(这里是包含目录下的文件的)
        for dir in dirs:
            path=upper_path+'\\'+dir
            if os.path.isdir(path):
                #print (path)
                #print ('Now analyze '+path)
                if os.path.exists(path) and path.split(':')[0].lower()!='c' :

                    filename=get_filename(path)


                    #print filename
                    havelog = 0
                    for i  in filename:

                        if os.path.splitext(i)[1][1:].lower() =='log' and 'test.log' not in i: #找出log文件

                            createtime=get_filecreatetime(i)
                            timedelt=(nowtime - createtime ).days
                            if timedelt>7:
                                print ('The export have not executed '+timedelt+' Days')
                            havelog=havelog+1
                            try:
                                f = open(i,"r")
                                n=0
                                for line in f.readlines():
                                    if 'terminated successfully' in line:
                                        n=n+1
                                f.close()
                                if n==0:
                                    print('Export Job had failed in ' + str(i))


                            except Exception as e:
                                print (e)
                        else:
                            pass

                    if havelog==0:
                        print ('There is no log in '+str(path))

                    #print destpath
                else:
                    print ('请输入正确的路径')
                #break
