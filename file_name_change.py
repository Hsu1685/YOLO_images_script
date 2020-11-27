import os
import datetime

path_1 = 'train_images_2 - コピー/'
path_2 = 'train_labels_2 - コピー/'

extension_1 = '.jpg'
extension_2 = '.xml'


def mycompare(name):
    name = name[name.find('_') + 1:name.find('.')]
    return(int(name))

def rename(path, extension):
    # 得到今天的時間
    today = datetime.date.today()    
    # 獲取該目錄下所有檔案，存入列表中
    file_name = os.listdir(path)
    # 所有檔案數量
    print('檔案數量:', len(file_name))
    # 列印第一筆檔名
    print('第一筆檔名:',file_name[0])
    # 列印第一筆檔名只帶數字
    print('第一筆檔名尾數字:',mycompare(file_name[0]))
    # 排序檔名清單(依照檔名尾所帶的數字)
    file_name_sorted = sorted(file_name, key=mycompare)
    # 顯示排序後的檔名
    print('排序後的檔名清單:',file_name_sorted)

    n = 0

    for i in file_name_sorted:
        # 設定舊檔名
        oldname = i
        # 設定新檔名(格式: 今天的時間_流水號)
        newname = str(today) + '_' + str(n+1) + extension
        # 用os模組中的rename方法對檔案改名
        os.rename(path+oldname, path+newname)
        print(oldname, '======>', newname, 'renamed')
        n += 1

if __name__ == "__main__":
    rename(path_1, extension_1)
    # rename(path_2, extension_2)