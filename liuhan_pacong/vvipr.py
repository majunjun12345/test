#coding:utf-8

import requests
from pyquery import PyQuery as pq
import os
import time


"""
要模拟点击

根据页码分段缓存
"""


class Model():
    """
    基类, 用来显示类的信息
    """

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Patent(Model):
    """
    存储电影信息
    """

    def __init__(self):
        self.num = 0
        self.patent_num = 0
        self.apply_date = ""
        self.title = ''
        self.owner = ''
        self.owner_addr = ""
        self.grant_date = ""


def cached_page(url):
    """
    缓存, 避免重复下载网页浪费时间
    """
    folder = '页面缓存'
    # 建立 cached 文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)

    # https://movie.douban.com/top250?start=100
    filename = '{}.html'.format(url.split('=', 1)[1])
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        # 发送网络请求, 把结果写入到文件夹中
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def data_from_div(div):
    """
    从一个 div 里面获取到一个电影信息
    """
    e = pq(div)

    # 小作用域变量用单字符
    patent = Patent()
    patent.num = e('.w06').text()
    patent.patent_num = e('.w07').text()
    patent.apply_date = e('.w07').text()
    patent.title = e('a').attr("title")
    patent.owner = e('.w14').text()
    patent.owner_addr = e('.w14').text()
    patent.grant_date = e('.w07').text()
    # m.owner_addr = e('.pic').find('em').text()
    return patent


def data_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的电影
    """
    page = cached_page(url)
    e = pq(page)
    items = e('.small mrr nobor')
    # 调用 movie_from_div
    datas = [data_from_div(i) for i in items]
    return datas


def main():
    url = "https://www.vvipr.com/zpro/pall.htm"
    data = data_from_url(url)


if __name__ == "__main__":
    main()