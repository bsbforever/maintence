#coding:UTF8
import time
import datetime
import os
import os.path
import shutil
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
    nums = [ '01','02','03','04','06','07','08','09']
    for aoi in nums:
        upper_path=r'd:\smt_aoi_spi\AOI'+aoi+r'\JET7000E_SPC\1_R'
        #print (upper_path)

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
                        if os.path.splitext(i)[1][1:].lower() not  in ['db','ini','pdf','prg','mdb','off']\
                                and ('data' in i.lower() or 'image' in i.lower()):
                            try:
                                modtime=get_filecreatetime(i)

                                timedelt=(nowtime - modtime ).days
                                if timedelt>90:
                                    print (str(i) +' 已经'+str(timedelt)+'天未修改')
                                    os.remove(i)

                            except Exception as e:
                                print (e)
                        else:
                            #print (str(i)+' specail extentions,not deleted')
                            pass
                    #print destpath
                else:
                    print ('请输入正确的路径')
                #break
