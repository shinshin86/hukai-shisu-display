# -*- coding: utf-8 -*-
import sys

argvs = sys.argv
argc = len(argvs)

# 引数の数が違う際は処理を行わない
if (argc != 3):
    print "温度 湿度の順で引数を２つ入力してください"
    quit()

print "温度 : " + argvs[1] 
print "湿度 : " + argvs[2]

# 不快指数の計算処理
hukai_shisu_result = 0.81 * float(argvs[1]) + 0.01 * float(argvs[2]) * (0.99 * float(argvs[1]) - 14.3) + 46.3

print "本日の不快指数 : " + str(hukai_shisu_result)
