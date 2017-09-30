# -*-coding:utf-8 -*-
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
from stations import stations
import requests
import urllib3


def cli():
    """command-line interface"""
    arguments = docopt (__doc__)
    from_station = stations.get (arguments['<from>'])
    to_station = stations.get (arguments['<to>'])
    date = arguments['<date>']
    urllib3.disable_warnings ()
    url0 = 'https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format (
        date, from_station, to_station)
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format (
        date, from_station, to_station)
    print (url)

    # 添加verify=False参数不验证证书
    r0 = requests.get (url0, verify=False)
    r = requests.get (url, verify=False)
    print (r0.json ())
    print (r.json ())


if __name__ == '__main__':
    cli ()
