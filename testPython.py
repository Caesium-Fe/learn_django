import math
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from functools import wraps
from typing import Dict

from unittest import TestCase

class TestMultiThread(TestCase):
    # def fund_thread(func):
    #     # @warps(func)
    #     def inner(*args, **kwargs):
    #         p = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
    #         p.start()
    #         # thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    #         # thread.start()
    #
    #     return inner
    def fund_thread(func):
        # @warps(func)
        def inner(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.start()

        return inner


    # def fund_thread(func):
    #     # @warps(func)
    #     # with ThreadPoolExecutor() as executor:
    #     pool = ThreadPoolExecutor(max_workers=5)
    #
    #     def inner(*args, **kwargs):
    #         result = pool.submit(func, args, kwargs)
    #         # print(result)
    #
    #     return inner

    #
    # @fund_thread
    # def showA(A, B='cnm'):
    #     time.sleep(2)
    #     print(A)
    #     print(B)
    #
    #
    # @fund_thread
    # def showB(C):
    #     print(C)
    #


class TestRequest(TestCase):
    
    def request_sb(requests):
        requests.request('GET', 'http://10.197.24.246:9000/show/info')
    

    def test_request_jiaban(self):
        # 测验以下是什么问题导致返回状态码407，结果是环境变量中设置了代理。
        import requests
        from datetime import datetime
        url = r'http://10.175.94.58:8088/report_message_four/'
        # url = r'http://10.175.94.58:8088/reportform/'
        # headers = {
        #     "Cookie": "csrftoken=alx93ODoiD11x1txXxEV9mnMPsvkIHagATCLUDvIcJhaLaSjTRpS9eG1EkKPJ7y2;eerf_user=F1241948",
        #     "Host": "10.175.94.58:8088",
        #     "Origin": "http://10.175.94.58:8088",
        #     "Referer": "http://10.175.94.58:8088/reportform/",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        # }
        data = {
            "selectedLeader": "All",
            "selectedTeam": "All",
            "_time": datetime.now().strftime('%Y-%m-%d'),
            # "_time": '2023-10-5',
            "selected_22_dep": "All"
        }
        response = requests.post(url=url, data=data)
        # response = requests.get(url=url)
        print(response.status_code)



class TestPandas(TestCase):

    def load_excel():
        import pandas as pd
        df = pd.read_excel(r'F:\bug\20230428_otacorrelation\Correlation Keyword.xlsx')
        print(df)


class TestColor(TestCase):

    @staticmethod
    def yanse():
        import random
        color = ["#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])]
        print(color)

    def test_gradient_color(self):
        s = TestColor.gradient_color('9F841B', '52308A', 10)
        print(s)

    @staticmethod
    def gradient_color(start_color, end_color, colornums):
        import numpy as np
        '''
        start_color:初始颜色代码（不要带#）
        end_color:结尾颜色代码（不要带#）
        colornums:颜色个数
        return:colornums个渐变颜色代码
        '''
        return ['#%06x' % int(i) for i in np.linspace(int(start_color, 16), int(end_color, 16), colornums)]
    
class TestDrawMultiPic(TestCase):

    def test_multi_hist(self):
        sample1 = [1, 1, 1, 1, 2, 2, 4, 5, 3, 6, 6, 6, 6, 6, 10, 10, 10, 15, 15]
        sample2 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
        sample3 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
        sample4 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
        sample5 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
        data = [sample1, sample2, sample3, sample4, sample5]
        TestDrawMultiPic.multi_hist(data, title="hospital_patient", xlabel="hospitals", ylabel="patients")

    @staticmethod
    def multi_hist(data, title="hospital_patient", xlabel="hospitals", ylabel="patients", bins=16):
        import matplotlib.pyplot as plt
        import numpy as np
        # data : shape = M*N
        # assert len(np.shape(data))==2, r"数据要二维度的"
        title = r"Histogram with '{}' bins".format(title)
        xlabel = r"{}_({})".format(xlabel, "M")
        ylabel = r"{}_({})".format(ylabel, "M")
        num = len(data)
        label = [r"bar. - {}".format(str(i)) for i in range(num)]
        color = [j for i, j in zip(range(num), ['r', 'g', 'b', 'y', 'b'])]
        plt.hist(  ## 绘制数据直方图
            x=data,  # 输入数据 - 自动统计相同元素出现的数量
            bins=bins,  # 指定直方图的条形数为20个
            edgecolor='w',  # 指定直方图的边框色
            color=color,  # 指定直方图的填充色
            label=label,  # 为直方图呈现图例
            # density=False,  # 是否将纵轴设置为密度，即频率
            # alpha=0.8,      # 透明度
            # rwidth=1,       # 直方图宽度百分比：0-1
            # stacked=False
        )  # 当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放
        s = np.arange(len(data[0]))
        plt.xticks(s, data[0])
        ax = plt.gca()
        ax.set_xticks(s)
        # 显示图例
        plt.title(s=title)
        plt.xlabel(s=xlabel)
        plt.ylabel(s=ylabel)
        plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0, prop={'size': 8}, shadow=False)
        # 显示图形
        # plt.show(bbox_inches='tight')
    
        plt.savefig('a.png', bbox_inches='tight')
        plt.close()

    def test_draw_scatter(self):
        data1 = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7]]
        data2 = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7]]
        TestDrawMultiPic.draw_scatter(data1, data2)

    def draw_scatter(data1, data2):
        import matplotlib.pyplot as plt
        l_d = len(data1)
        f, (ax0) = plt.subplots(1, 1, figsize=(19.6, 7.2))
        plt.subplots_adjust(top=0.9, bottom=0.25, left=0.05, right=1, hspace=0, wspace=0.08)
        for i in range(l_d):
            plt.scatter(data1[i], data2[i], label=str(i))
        plt.legend(ncol=3)
        # handles, labels = plt.gca().get_legend_handles_labels()
        # order = [0, 3, 1, 2]
        # plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order], ncol=3)
        # plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0, prop={'size': 8}, shadow=False, ncol=3)
        # plt.show(bbox_inches='tight')
        plt.savefig('a.png', bbox_inches='tight')
        plt.close()


    def draw_bar():
        import matplotlib.pyplot as plt
        import numpy as np

        fig, ax = plt.subplots(1, 1, figsize=(19.6, 7.2))
        plt.subplots_adjust(top=0.9, bottom=0.25, left=0.05, right=1, hspace=0, wspace=0.08)

        x = np.arange(5)
        y = [-90, 10, 40, 50, 10]
        y1 = [20, 60, 30, 80, 50]
        y2 = [20, 60, 30, 80, 50]

        bar_width = 0.1
        tick_label = ["A", "B", "C", "D", "E"]

        plt.bar(x, y, bar_width, align="center", color="red", label="项目A", alpha=0.5)
        plt.bar(x + bar_width, y1, bar_width, color="blue", align="center", label="项目B", alpha=0.5)
        plt.bar(x + bar_width * 2, y2, bar_width, color="yellow", align="center", label="项目c", alpha=0.5)

        plt.xlabel("种类")
        plt.ylabel("数量")

        plt.xticks(x + bar_width, tick_label)

        plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0, prop={'size': 8}, shadow=False)

        plt.savefig('a.png', bbox_inches='tight')
        # plt.show()


    def draw_scatter(data):
        import matplotlib.pyplot as plt
        plt.scatter(data[0], data[1])
        plt.plot([1, 7], [1 * 7 + 0, 1 * 1 + 0], color='black')
        plt.plot([1, 7], [1 * 7 - 1, 1 * 1 - 1], color='black')
        plt.plot([1, 7], [1 * 7 + 1, 1 * 1 + 1], color='black')
        plt.show()
        pass


    def draw_scatter2(data):
        import matplotlib.pyplot as plt
        plt.scatter(data[0], data[1])
        plt.plot([data[0][0], data[0][-1]], [1 * data[1][0] + 0, 1 * data[1][-1]], color='black')
        plt.plot([data[0][0], data[0][-1]], [1 * data[1][0] - 1, 1 * data[1][-1] - 1], color='black')
        plt.plot([data[0][0], data[0][-1]], [1 * data[1][0] + 1, 1 * data[1][-1] + 1], color='black')
        plt.show()
        pass

    def test_draw_predict_scatter(self):
        import numpy as np
        chamber = np.random.randint(2,30,size=(13,3))
        omnia = np.random.randint(2,30,size=(13,3))
        y_label = 'asd'
        x_axis = np.random.randint(2,30,size=(13,1))
        pic_title = 'asdasdasd'
        pic_save_path = r'F:\bug\20230324_otacorrelation\demand 20230323 data\1'
        predict_plot_keyword = 'asd'
        TestDrawMultiPic.draw_predict_scatter(chamber, omnia, y_label, x_axis, pic_title, pic_save_path, predict_plot_keyword)

    def draw_predict_scatter(chamber, omnia, y_label, x_axis, pic_title, pic_save_path, predict_plot_keyword):
        """
        散点图
        :params chamber: original chamber's data
        :params omnia: original ota's data
        :params y_label: ota data's sheet name
        :params x_axis: short item
        :params pic_title: picture title name
        :params pic_save_path: picture save path
        :return:
        """
        import os
        import matplotlib.pyplot as plt

        try:
            if 'x-axis' in predict_plot_keyword[0]['key']:
                x_range = float(predict_plot_keyword[0]['value'])
                y_range = float(predict_plot_keyword[1]['value'])
            elif 'y-axis' in predict_plot_keyword[1]['key']:
                x_range = float(predict_plot_keyword[1]['value'])
                y_range = float(predict_plot_keyword[0]['value'])
            else:
                x_range = y_range = 3.0
        except Exception as e:
            x_range = y_range = 3.0
        c_middle, c_avg = TestDrawMultiPic.__get_middle_number(chamber)
        o_middle, o_avg = TestDrawMultiPic.__get_middle_number(omnia)

        legend_num = len(chamber)
        marker = ['o', 's', '^']
        color_start_list = ['33567F', '823331', '687E3A']
        color_end_list = ['CDD6E6', 'E7CDCD', 'FBCDB7']

        if legend_num % 3:
            color_change_number = legend_num // 3 + 1
        else:
            color_change_number = legend_num // 3
        # 渐变色列表
        color_list = [TestDrawMultiPic.__gradient_color(color_start_list[i], color_end_list[i], color_change_number) for i in range(3)]

        fig, ax = plt.subplots(1, 1, figsize=(19.6, 7.2))
        plt.subplots_adjust(top=0.9, bottom=0.25, left=0.05, right=1, hspace=0, wspace=0.08)
        for i in range(legend_num):
            x_data = chamber[i]
            y_data = omnia[i]
            icon_flag = i % 3  # used to determine icons and colors
            color_flag = i // 3  # used to determine colors
            plt.scatter(x_data, y_data, marker=marker[icon_flag], color=color_list[icon_flag][color_flag],
                        label=x_axis[i])
        plt.ylabel(y_label)
        plt.xlabel('Chamber')
        plt.title(pic_title + ' Correlation', fontsize=24, color="black", fontdict={'family': 'monospace'},
                verticalalignment="bottom")
        # 图例个数逻辑：20個標註以內畫一排，20-40個畫兩排，40個以上畫三排。
        if len(x_axis) <= 20:
            col_num = 1
        elif 20 < len(x_axis) <= 40:
            col_num = 2
        else:
            col_num = 3
        ax.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0, prop={'size': 8}, shadow=False, ncol=col_num)
        ax.set_xlim([c_middle - x_range, c_middle + x_range])
        ax.set_ylim([o_middle - y_range, o_middle + y_range])

        try:
            if 'v' in predict_plot_keyword[2]['value'].lower():
                # 绘制一次函数 y = kx + b， 绘制逻辑：1.有keyword中规定的标识，则画 y=x; 2.没有标识，则用x和y轴平均值来计算y轴偏移量(b)的值
                max_c = c_middle + x_range
                min_c = c_middle - x_range
                max_o = o_middle + y_range
                min_o = o_middle - y_range
                intercept = 0
            else:
                # 绘制一次函数 y = kx + b， 绘制逻辑：1.有keyword中规定的标识，则画 y=x; 2.没有标识，则用x和y轴平均值来计算y轴偏移量(b)的值
                max_c = c_avg + x_range
                min_c = c_avg - x_range
                max_o = o_avg + y_range
                min_o = o_avg - y_range
                intercept = o_avg - c_avg
        except Exception:
            max_c = c_middle + x_range
            min_c = c_middle - x_range
            max_o = o_middle + y_range
            min_o = o_middle - y_range
            intercept = 0
        try:
            if predict_plot_keyword[3]['value']:
                b_intercept = predict_plot_keyword[3]['value'] + intercept
            else:
                b_intercept = 1 + intercept
        except Exception:
            b_intercept = 1 + intercept
        plt.plot([min_c, max_c], [1 * min_o + intercept, 1 * max_o + intercept], color='black')
        plt.plot([min_c, max_c], [1 * min_o - b_intercept, 1 * max_o - b_intercept], color='black')
        plt.plot([min_c, max_c], [1 * min_o + b_intercept, 1 * max_o + b_intercept], color='black')

        # plt.show()
        plt.savefig(os.path.join(pic_save_path, pic_title + ' Correlation.png'), bbox_inches='tight')
        plt.close(fig)
        pass

    def __get_middle_number(data):
        """
        get the middle number and the mean number in the list data
        """
        c = []
        data_1 = [c.extend(list(i)) for i in data]
        c.sort()
        half = len(c) // 2
        return (c[half] + c[~half]) / 2, sum(c) / len(c)
    
    def __gradient_color(start_color, end_color, colornums):
        import numpy as np
        '''
        start_color:初始颜色代码（不要带#）
        end_color:结尾颜色代码（不要带#）
        colornums:颜色个数
        return:colornums个渐变颜色代码
        '''
        return ['#%06x' % int(i) for i in np.linspace(int(start_color, 16), int(end_color, 16), colornums)]
    
    def test_draw_box_plot(self):
        from matplotlib import pyplot as plt
        fig = plt.figure(figsize=(20, 5), dpi=100)
        ax = fig.add_subplot(111)
        # ax.boxplot([[10,2,3,4],[1,-2,3,4],[1,2,3,4]], sym=None)
        # ax.boxplot([[10,2,3,4],[1,-2,3,4],[1,2,3,4]])
        # ax.boxplot([(1,2,3,4), (1,2,3,4), (1,2,3,4), (1,2,3,4), ])
        # ax.boxplot([[1,2,3,4],[1,2,3,4],[1,2,3,4]], sym='.')
        # ax.boxplot([[10,2,3,-4, 100],[1,-2,3,14, -100],[1,2,3,24, -10]], sym='')
        # ax.boxplot([[10,2,3,-4, 100],[1,-2,3,14, -100],[1,2,3,24, -10]], sym=None, whis=1.5)
        box = ax.boxplot([[10,2,3,-4, 100],[1,-2,3,14, -100],[1,2,3,24, -10]], sym=None, whis=1.5)
        # for each in zip(box['boxes'], ):
        #     each.set_facecolor('red')
        # plt.show()
        # plt.plot([1, None, 2, None], mark='o')
        plt.xticks([1,2,3,4], ['1', None, 3.2, 1])
        plt.xticks([7,1,5], [7,1,5])
        # plt.plot([1,5,7,9], [1, 3, 2,4])
        plt.tick_params(axis='x', labelsize='large')
        # plt.tick_params(top='on', right='on', which='both')
        # ax.set_xlim([3, 5])
        # plt.plot([1,2,3,4], [1])
        # ax.plot([None]*2, [0,4])
        # plt.xticks([2], ['2'])
        plt.show()


class TestSolution:

    # def __init__(self):
    # count = 0

    # def numberOfSteps(self, num: int) -> int:
    #     if num:
    #         self.count += 1
    #     else:
    #         return self.count

    #     if num % 2:
    #         num -= 1
    #         self.numberOfSteps(num)
    #     else:
    #         num = num // 2
    #         self.numberOfSteps(num)

    def test_sort_item(self):
        # 测试排序方法
        # functools.cmp_to_key 方法用最终结果为正负来判断谁大谁小
        import re
        import operator
        import functools
        data_list = ['a9', '7', 'b1', '1', '11', 'a', 'aa', '3']
        data_list.sort(key=functools.cmp_to_key(_two))
        print(data_list)
        # 这个方法用来排序数字和字符一起存在的情况。
        def _two(value1, value2):
            c = None
            if value1 and re.match(r"[+-]?\d+(\.\d+)?([eE][+-]?\d+)?", value1):
                c = float(value1)
            d = None
            if value2 and re.match(r"[+-]?\d+(\.\d+)?([eE][+-]?\d+)?", value2):
                d = float(value2)
            if c and not d:
                return -1
            elif not c and d:
                return 1
            elif c and d:
                if c < d:
                    return -1
                elif c > d:
                    return 1
                else:
                    return 0
            elif value1 and value2:
                if operator.lt(value1, value2):
                    return -1
                elif operator.gt(value1, value2):
                    return 1
                else:
                    return 0
            else:
                return 0



class TestFullScreen(TestCase):

    def test_full_screen(self):
        import time
        import subprocess

        while True:
            # 获取当前活动窗口标题
            active_window_title = subprocess.check_output(["powershell", "(Get-Process | Where-Object {$_.MainWindowTitle}).MainWindowTitle"]).decode("latin-1").strip()

            # 判断当前活动窗口是否是全屏游戏
            if active_window_title != "":
                print("当前活动窗口标题:", active_window_title)
                print("可能是全屏游戏，进行进一步检测...")

                # 进一步检测是否是全屏窗口
                is_fullscreen = subprocess.check_output(["powershell", "(Get-Process | Where-Object {$_.MainWindowTitle -eq '"+active_window_title+"' }).Responding"]).decode("latin-1").strip()

                if is_fullscreen == "True":
                    print("当前窗口处于全屏模式！")
                    # 在这里可以记录日志或采取其他操作，例如发送警报
                    # 你也可以添加更多的逻辑来判断是否有其他进程干扰全屏游戏
                else:
                    print("当前窗口不是全屏模式。")
            else:
                print("当前没有活动窗口。")

            # 等待一段时间后继续监测
            time.sleep(5)


class TestXuShu(TestCase):

    @staticmethod
    def test_xu_shu():
        print(3+5j)


class TestTriangleArea(TestCase):

    # @staticmethod
    def test_triangle_area(self):
        # a = float(input('a = '))
        # b = float(input('b = '))
        # c = float(input('c = '))
        a = 1
        b = 2
        c = 2.5
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            print('周长: %f\n' % (a + b + c))
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            print('面积: %f' % (area))
            print()
        else:
            print('不能构成三角形')

    def test_create_triangle(self):
        for i in range(5):
            for _ in range(5 - i - 1):
                print(' ', end='')
            # for _ in range(2 * i + 1):
            for _ in range(2*i - 1):
                print('*', end='')
            print()

    def test_feibolachi(self):
        # def feibolachi(n):
        #     if n<1:
        #         return 0
        #     elif n == 1 or n == 2:
        #         return 1
        #     else:
        #         return feibolachi(n-1) + feibolachi(n-2)
        # print(feibolachi(20))
        # print(result)

        # a = 1
        # tmp = 0
        # 前两位为固定值1，后面开始需要用到结果和前一位相加
        result = []
        # for i in range(20):
        #     if i<2:
        #         a = 1  # 结果
        #         pre = 1  # 前一位
        #         result.append(1)
        #         continue
        #     tmp = a  # 把上一次的结果保存下来
        #     a = a + pre  # 将结果保存
        #     pre = tmp  # 必须在这次计算结果以后，才能将上次的结果保存
        #     result.append(a)

        # 生成器来实现斐波拉切数生成
        def feibo_(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a+b
        
        for i in feibo_(101):
            result.append(i)

        # reduce函数  不太行
        # from functools import reduce
        # print(reduce(lambda x,y: x+y, range(1,101)))

        print(result)

    def test_search_wanmei_num(self):
        wms = []
        # 完美数是自身因数的和是这个数
        for i in range(1, 10000):
            result = 0
            # 只需要通过这个数的平方根以下的数，就能找到所有的因数了
            for inshu in range(1, int(math.sqrt(i))+1):
                # 若果整除，则是因数
                if i % inshu == 0:
                    # 整除直接先加上这个因数
                    result += inshu
                    # 再来判断另外一个因数不能是1和重复值，不是直接加
                    if inshu != 1 and i // inshu != inshu:
                        result += i // inshu
            if result == i:
                wms.append(i)
        print(wms)

    def test_search_sushu(self):
        # res = []
        # 素数是只有1和自身为除数的数 
        # 纯暴力解法
        # for i in range(1, 1001):
        #     c = 0
        #     for j in range(1, i+1):
        #         if i % j == 0:
        #             if j != 1 and i != j:
        #                 break
        #             else:
        #                 c += 1
        #         else:
        #             ...
        #     if c == 2:
        #         res.append(i)
        #     else:
        #         ...
        # print(res)
        # num = 100
        # 少一部分计算
        resu = []
        for j in range(2, 1001):
            for i in range(2, int(math.sqrt(j))+1):
                if not j % i:
                    break
                elif j == 2:
                    break
            else:
                resu.append(j)
        print(resu)
        return resu

    def test_for_else(self):
        for ii in range(100):
            if ii == 3:
                break
        else:
            print(1)


    def test_max_yue_min_bei(self):
        # 求最大的公约数和最小的公倍数
        a = 100
        b = 10
        c = min(a,b)  # 取出最小的数
        for i in range(1, c+1):
            tmp = 0
            if a % i == 0 and b % i == 0:
                tmp = tmp if i < tmp else i
        print(tmp)
        d = a*b  # 最大的公倍数
        # 遍历思想解决获取公倍数
        for i in range(1, d+1):
            if i % a == 0 and i % b == 0:
                print(i)
                break
        else:
            print(d)
        # 最小公倍数就是两个数的乘积除以最大公约数
        res = d / tmp
        print(res)

    def test_huiwen(self, num):
        # 实现判断一个数是不是回文数的函数
        # num = 101
        tmp = num
        tot = 0
        while tmp > 0:
            tot = tot * 10 + tmp % 10
            tmp = tmp // 10  # / 和 // 表达的意思不同，前面算出float，后面算出int
        # print(tot == num)
        return tot == num

    def test_sushu(self):
        res = []
        sushu = self.test_search_sushu()
        for i in sushu:
            if self.test_huiwen(i):
                res.append(i)
        print(res)
        # return res

class Test_queue(TestCase):

    def test_is_queue(self):
        import queue
        q1 = queue.Queue()
        q2 = queue.Queue()
        q1.put(1)
        q2.put(2)
        print(q2.get())


class Product:

    def __init__(self) -> None:
        self.name: str = ''
        self.price: float = 0.0
        self.has_amount: int = 0

    def __hash__(self) -> int:
        return hash(self.has_amount)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Product):
            return self.__hash__() == __value.__hash__()
        return False

class Shop_car:

    def __init__(self):
        self.shop_car: Dict[Product, int] = {}

    def add_item(self, product, buy_amount):
        self.shop_car[product] = buy_amount

    def check_out(self):
        total_cost = 0
        for p, a in self.shop_car.items():
            total_cost += p.price * a
        print(total_cost)

class Test_shop_car(TestCase):

    def test_add_item(self):
        sp = Shop_car()
        p1 = Product()
        p1.name = 'iphone'
        p1.price = 100
        p1.has_amount = 10
        p2 = Product()
        p2.name = 'ipad'
        p2.price = 1000
        p2.has_amount = 10
        sp.add_item(p1, 10)
        sp.add_item(p2, 10)
        print(hash(p1))
        print(hash(p2))
        print(hash(p2) == hash(p1))
        my_set = {p1}
        # 当只重写了hash函数，那么这里p2还是不在set中
        # 原因为set虽然用hash来排序，但是判断是否在其中，
        # 还会比对eq方法的返回值，所以这里会是False
        print(p2 in my_set)
        # return sp

    def test_check_out(self):
        sp = self.test_add_item()
        sp.check_out()


class Test_str(TestCase):

    def test_string(self):
        str1 = 'wu,Han'
        print(str1.capitalize())

    def test_for_prt(self):
        print('buy {0} is costing {1} rmb'.format('asd', 1000))
        print('buy %s is costing %d rmb' % ('asd', 1000))


    def test_list(self):
        p1 = Product()
        p1.name = 'phone'
        p2 = Product()
        p2.name = 'pad'
        l1 = [p1, p2]
        # l1 = (p1, p2)  # 元组也没用，还是会被修改
        # l2 = [p1, p2]
        # from copy import deepcopy
        # l2 = deepcopy(l1)
        l2 = l1
        # l2 = l1[:]
        # l2 = list(l1)
        # l2 = l1.copy()
        # l1[1].name = 'xiaochou'
        l3 = self.xiu_gai(l1)
        print(l1[1].name)
        print(l2[1].name)
        print(l3[1].name)

    def xiu_gai(self, l):
        l1 = l
        l1[1].name = 'xiaochou'
        return l1
    
    def test_set_s(self):
        a = set((1,2,3,4,5,6))
        a.discard(1)
        a.remove(2)
        a.update([1,2,3])
        a.pop()
        print(a)

    def test_set_c(self):
        a = set((1,2,3,4,5,6))
        b = set((3,4,5,6,7,8))
        print(a-b)  # 单边差集
        print(a.difference(b))
        print(a.symmetric_difference(b)) # 双边差集W
        print(a^b)
        print(a|b)  # 并集
        print(a.union(b))
        print(a&b)  # 交集
        print(a.intersection(b))

    def test_paoma(self):
        import os
        st = "123"
        for _ in range(100):
            os.system('cls')
            print(st)
            time.sleep(0.2)
            st = st[1:] + st[0]

    def test_yanzhengma(self):
        """
        生成指定长度的验证码

        :param code_len: 验证码的长度(默认4个字符)

        :return: 由大小写英文字母和数字构成的随机验证码
        """
        import random
        code_len = 4
        all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        last_pos = len(all_chars) - 1
        code = ''
        for _ in range(code_len):
            index = random.randint(0, last_pos)
            code += all_chars[index]
        return code

    def test_jidu(self):
        total = [True] * 30
        index = 1
        drop_index = set()
        # for i in range(1, 31):
        #     if index != 9:
        #         index += 1
        #     else:
        #         index = 1
        #         drop_index.add(i)
        #     if len(drop_index) == 15:
        #         break
        i = 0
        while len(drop_index) < 15:
            if total[i]:
                if index == 9:
                    index = 1
                    total[i] = False
                    drop_index.add(i)
                index += 1
            i += 1
            i = i % 30
        print(list(drop_index))

class Test_re(TestCase):

    def test_re(self):
        import re
        #需要筛选 所有以0开头，后面跟着2-3个数字，然后是一个连字号“-”，最后是7或8位数字的字符串
        str_1 = 'asd028-12345678或0813-7654321asd'
        re_c = re.compile('0\d{2,3}-\d{7,8}')
        print(re.search(re_c, str_1))

class Test_multiprocess(TestCase):

    @staticmethod
    def down_load(filename):
        from random import randint
        from os import getpid
        from time import sleep
        print('启动下载进程，进程号[%d].' % getpid())
        print('开始下载%s...' % filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

    def test_download(self):
        from time import time
        t1 = time()
        # 1.创建进程的 multiprocessing的pool 方法
        # from multiprocessing import Pool
        # with Pool() as pool:
            # results = pool.map(self.down_load, ('asd.txt', 'ddd.txt'))
            # for result in results:
            #     print(result)
        # 2.创建进程的 concurrent.futures的ProcessPoolExecutor 方法
        from concurrent.futures import ProcessPoolExecutor
        import os
        with ProcessPoolExecutor(min(32, int(os.cpu_count() * 65/100) or 1)) as executor:  # 甚至可以指定核心数量
            results = executor.map(self.down_load, ['asd.txt', 'ddd.txt'])
            # futures = [executor.submit(self.down_load, i) for i in ['asd.txt', 'ddd.txt']]
            # for future in futures:
            #     print(future.result())
        t2 = time()
        print('total cost time {0}'.format(t2-t1))

    @staticmethod
    def sub_task(args):
        queue, string = args  # 这里需要把传递进来的args解开后进行使用
        import time
        while True:
            a = queue.get()
            if a >= 10:
                # 这里不把计数的值再次放入队列，别的进程无法正常结束
                queue.put(a)
                break
            print(string)
            queue.put(a + 1)
            time.sleep(0.02)
    
    def test_jinchengtongxin(self):
        from multiprocessing import Pool, Manager
        man = Manager()
        queue = man.Queue()  # 这里无法直接创建队列用于进程通信，需要创建manager对象后，再创建队列
        queue.put(0)
        args = [(queue, i) for i in ['Ping', 'Pong']]
        with Pool() as pool:
            pool.map(self.sub_task, args)  # 这里的参数没有办法传递两个，所以只能拼成args
            # pool.map(self.sub_task, (queue, queue), ('Ping', 'Pong'))
        # Process.daemon = True
        # Process(target=self.sub_task, args=(queue, 'Ping',)).start()
        # Process(target=self.sub_task, args=(queue, 'Pong',)).start()

        
    def test_jicheng(self):
        from threading import Thread
        import time
        class MultiDown(Thread):

            def run(self) -> None:
                time.sleep(3)
                print('finish...')
                # return super().run()

        print(time.time())
        # 守护线程的作用是当主程序结束时，子线程直接结束。当不设为守护线程，则主程序结束，子线程任然会执行完毕。
        # MultiDown(daemon=False).start()
        MultiDown(daemon=True).start()
        # time.sleep(4)
        print(time.time())

    @staticmethod
    def count(args):
        list1, queue1 = args
        tmp = 0
        for i in list1:
            tmp += i
        queue1.put(tmp)

    def test_fen_ren_wu(self):
        from multiprocessing import Pool, Manager, Queue
        import os

        cpu_num = os.cpu_count()
        total_list = [x for x in range(1,1000001)]
        total = 0
        for i in total_list:
            total += i
        print(total)
        # renwu_list = [total_list[]]
        renwu_list = []
        for i in range(cpu_num+1):
            renwu_list.append(total_list[i*int(len(total_list)/cpu_num): (i+1)*int(len(total_list)/cpu_num)])
        man = Manager()
        queue1 = man.Queue()
        args = [(list1, queue1) for list1 in renwu_list]
        with Pool(cpu_num) as pool:
            # pool.map(self.count, args)
            # pool.map(lambda args: count(*args), [(list1, queue1) for list1 in renwu_list])  # 并不能序列化(pickle) lambda函数
            pool.map(self.count, [(list1, queue1) for list1 in renwu_list])
        total = 0
        while not queue1.empty():
            total += queue1.get()
        print(total)

    # DrissionPage 爬虫技术代替selenium技术

    def test_smtp(self):
        from smtplib import SMTP
        from email.header import Header
        from email.mime.text import MIMEText
        # 请自行修改下面的邮件发送者和接收者
        sender = 'abcdefg@126.com'
        receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
        message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
        message['From'] = Header('王大锤', 'utf-8')
        message['To'] = Header('骆昊', 'utf-8')
        message['Subject'] = Header('示例代码实验邮件', 'utf-8')
        smtper = SMTP('smtp.126.com')
        # 请自行修改下面的登录口令
        smtper.login(sender, 'secretpass')
        smtper.sendmail(sender, receivers, message.as_string())
        print('邮件发送完成!')

    def test_smtp_fujian(self):
        from smtplib import SMTP
        from email.header import Header
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.mime.multipart import MIMEMultipart
        import urllib

        # 创建一个带附件的邮件消息对象
        message = MIMEMultipart()

        # 创建文本内容
        text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
        message['Subject'] = Header('本月数据', 'utf-8')
        # 将文本内容添加到邮件消息对象中
        message.attach(text_content)

        # 读取文件并将文件作为附件添加到邮件消息对象中
        with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
            txt = MIMEText(f.read(), 'base64', 'utf-8')
            txt['Content-Type'] = 'text/plain'
            txt['Content-Disposition'] = 'attachment; filename=hello.txt'
            message.attach(txt)
        # 读取文件并将文件作为附件添加到邮件消息对象中
        with open('/Users/Hao/Desktop/汇总数据.xlsx', 'rb') as f:
            xls = MIMEText(f.read(), 'base64', 'utf-8')
            xls['Content-Type'] = 'application/vnd.ms-excel'
            xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
            message.attach(xls)

        # 创建SMTP对象
        smtper = SMTP('smtp.126.com')
        # 开启安全连接
        # smtper.starttls()
        sender = 'abcdefg@126.com'
        receivers = ['uvwxyz@qq.com']
        # 登录到SMTP服务器
        # 请注意此处不是使用密码而是邮件客户端授权码进行登录
        # 对此有疑问的读者可以联系自己使用的邮件服务器客服
        smtper.login(sender, 'secretpass')
        # 发送邮件
        smtper.sendmail(sender, receivers, message.as_string())
        # 与邮件服务器断开连接
        smtper.quit()
        print('发送完成!')

    def test_send_message(self):
        import urllib.parse
        import http.client
        import json

        host = "106.ihuyi.com"
        sms_send_uri = "/webservice/sms.php?method=Submit"
        # 下面的参数需要填入自己注册的账号和对应的密码
        params = urllib.parse.urlencode({'account': '1.2..30', 
                                         'password': '*******', 
                                         'content': 'blablabla...',
                                         'mobile': '13212341234',
                                         'format': 'json',
                                         })
        print(params)
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain',
        }
        conn = http.client.HTTPConnection(host, port=80, timeout=30)
        conn.request('POST', sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        jsonstr = response_str.decode('utf-8')
        print(json.loads(jsonstr))
        conn.close()

class Test_jinjie(TestCase):

    def test_shengchengshi(self):
        prices = {
            'AAPL': 191.88,
            'GOOG': 1186.96,
            'IBM': 149.24,
            'ORCL': 48.44,
            'ACN': 166.89,
            'FB': 208.09,
            'SYMC': 21.29
        }
        # 用股票价格大于100元的股票构造一个新的字典
        prices2 = {key: value for key, value in prices.items() if value > 100}  # 字典生成式
        print(prices2)
        prices3 = [{key: value} for key, value in prices.items() if value > 100]  # 列表生成式
        print(prices3)

    def test_liebiaoqiantaodekeng(self):
        names = ['关羽', '张飞', '赵云', '马超', '黄忠']
        courses = ['语文', '数学', '英语']
        # 录入五个学生三门课程的成绩
        # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
        scores = [[None] * len(courses)] * len(names)
        # scores = [[None] * len(courses) for _ in range(len(names))]
        for row, name in enumerate(names):
            for col, course in enumerate(courses):
                scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
                print(scores)

    def test_heapq(self):
        """
        从列表中找出最大的或最小的N个元素
        堆结构(大根堆/小根堆)
        """
        import heapq
        list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
        list2 = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        print(type(heapq.nlargest(3, list1)))
        print(heapq.nlargest(3, list1))
        print(heapq.nsmallest(3, list1))
        print(heapq.nlargest(2, list2, key=lambda x: x['price']))
        print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

    def test_itertools(self):
        """
        迭代工具模块
        """
        import itertools

        # 产生ABCD的全排列
        itertools.permutations('ABCD')
        # 产生ABCDE的五选三组合
        itertools.combinations('ABCDE', 3)
        # 产生ABCD和123的笛卡尔积
        itertools.product('ABCD', '123')
        # 产生ABC的无限循环序列
        itertools.cycle(('A', 'B', 'C'))

        print()

    def test_collections(self):
        """
        找出序列中出现次数最多的元素

        namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
        deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，
                而deque底层是双向链表，因此当你需要在头尾添加和删除元素时，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
        Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。
                    Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
        OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
        defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
        """
        from collections import Counter

        words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
            'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
            'look', 'into', 'my', 'eyes', "you're", 'under'
        ]
        counter = Counter(words)
        print(counter.most_common(3))

    def test_multi_sort_algorithm(self):
        item_yuan = [6,3,1,6,7,8,9,9,4,3,20,21,22,35,26,15,5,]
        """
        简单选择排序  找到最小于当前元素的下标，然后与当前元素位置互换
        """
        items = item_yuan[:]
        for i in range(len(items)-1):
            min_index = i
            for j in range(i+1, len(items)):
                if items[j] < items[min_index]:
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        print(items)

        """
        冒泡排序  两两元素比较，前大于后则，交换位置
        """
        items = item_yuan[:]
        for i in range(len(items)-1):
            for j in range(len(items)-1-i):
                if items[j] > items[j+1]:
                    items[j], items[j+1] = items[j+1], items[j]
        print(items)

        """
        冒泡排序升级版(搅拌排序)
        """
        items = item_yuan[:]
        for i in range(len(items) - 1):
            swapped = False
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True
            if swapped:
                swapped = False
                for j in range(len(items) - 2 - i, i, -1):
                    if items[j - 1] > items[j]:
                        items[j], items[j - 1] = items[j - 1], items[j]
                        swapped = True
            if not swapped:
                break
        print(items)

    def test_hebing(self):
        """
        两个有序数组合并成一个有序数组
        """
        items1 = [5,6,7,8,9]
        items2 = [1,2,3,4,5]
        index1,index2 = 0,0
        result = []
        while index1 < len(items1) or index2 < len(items2):
            if items1[index1] > items2[index2]:
                result.append(items1[index1])
                index1 += 1
            else:
                result.append(items2[index2])
                index2 += 1
        print(result)




