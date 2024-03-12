import math
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from functools import wraps

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
        for i in range(20):
            if i<2:
                a = 1  # 结果
                pre = 1  # 前一位
                result.append(1)
                continue
            tmp = a  # 把上一次的结果保存下来
            a = a + pre  # 将结果保存
            pre = tmp  # 必须在这次计算结果以后，才能将上次的结果保存
            result.append(a)
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
        # 素数是只有1和自身为除数的数
        for i in range(100):
            for j in range(i):
                if i % j == 0 or i == 1 and:
