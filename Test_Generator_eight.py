#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import random
import os
import sys

while True:
    inp_num = input("请输入要生成的行数：>>").strip()
    

    if inp_num.isdigit():
        data_type_lst = ["纯小写字母", "大小写混合"]
        
        while True:
            print("\n可选择的生成数据类型：")
            for i, data in enumerate(data_type_lst):
                print("\t",i, data)
                
            inp_data_type = input("\n请输入要生成数据的类型序号：>>").strip()
            
            if inp_data_type.isdigit() and inp_data_type in ["0","1"]:
                inp_data_type = int(inp_data_type)
                break
            else:
                print("输入无效，5s 后重新输入...")
                time.sleep(5)
                os.system("cls") 
        
        inp_fn = input("\n请输入一个文件保存的名字：>>").strip()
        inp_num = int(inp_num)
        
        # 去除重复值
        res_set = set()
        
        # 随机集
        random_set = []
        
        # 设定计时器
        start_time = time.time()
        
        # 添加 小写字母
        for i in range(97,123):
            random_set.append(str(chr(i)))
            
        # 添加 数字
        for i in range(10):
            random_set.append(str(i))
        
        # 添加大写字母        
        if inp_data_type:
            for i in range(65,91):
                random_set.append(str(chr(i)))
            
        # 记录生成的次数
        generator_num = 0
        
        # 写入文件
        file_obj = open(inp_fn, "w", encoding="utf-8")
            
        # 生成指定的值：
        while len(res_set) < inp_num:
            #temp_data = "".join(random.choices(random_set, k=8))
            # res_set.add(temp_data)
            res_set.add("".join(random.choices(random_set, k=8)))
            generator_num += 1
            
        # 生成完毕
        for i in res_set:
            # print("这是生成的密码: %s" % i)
            file_obj.write(str(i)+"\n")
            # pass
        else:
            print("共计用时：%.2f 秒，再见！" %(time.time() - start_time))
            print("共计 碰撞 了 %d 次" % generator_num)
            print("共占用了 %.3f MB的内存" % (sys.getsizeof(res_set)/1024/1024))
            # print("文件共占用了 %.3f MB的内存" % (sys.getsizeof(__file__)/1024/1024))
            # 统计内存占用的模块： pympler asizeof.asized(obj)
            # file_obj.close()
            time.sleep(5)
            break
            
    else:
        
        print("输入无效，5s 后重新输入...")
        time.sleep(5)
        os.system("cls")