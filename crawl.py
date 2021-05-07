import os
import sys
import json
import time
import pip._vendor.requests
import csv


class CRAWL:
    def __init__(self):
        self.seoul_dict={}
        self.tmp_list=[]
        self.data=[]
        self.write=[]
    
    def get_seoul(self):
        gu_list = []
        with open("seoul.txt","rt",encoding='UTF8') as f:
            for line in f:
                if line=='\n':
                    self.seoul_dict[key] = gu_list
                    gu_list = []
                    continue
                tmp = line.split(",")
                num = tmp[0];
                gu = tmp[1].replace("\n","")

                gu_list.append(gu)
                key= num
def get_json_value(self, key, i):
    try:
        if key in self.data["items"][i]:
            value = self.data["items"][i][key]
            self.write.append(value)
        else:
            self.write.append("None")
    except:
        self.stop = 1;

def crawling(self):
    f = open('test.csv','w',encoding='utf-8-sig', newline='')
    f.close()

    for num,gu_list in self.seoul_dict.items():
        print('-'+num)

        for gu in gu_list:
            print(' -'+gu)

            q = gu+'+'+u'맛집'
            display = 100

            self.stop = 0

            for start in range(1,6):
                url = 'https://store.naver.com/sogum/api/businesses?start='+str(start)+'&display='+str(display)+'&query='+q+'&sortingOrder=reviewCount'