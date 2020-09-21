import  requests

from  lxml import  etree
from urllib.parse import urljoin
import json
import csv
from functools import reduce
import re
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36" }


def ceshi():
    answer_list = []
    for page in range(21, 40):
        url="https://test.3uol.com/api/cafetest_list/"
        data={"action": "/api/cafetest_list/",
              "cid": "41",
              "size": "15",
              "page": page}
        request=requests.post(url,data,headers=headers,timeout=30).text
        html=etree.HTML(request)
        opreat=html.xpath('//div[@class="item clearfix"]/a/@href')


        for  o in opreat:
            daan = []
            n = 0
            kaishi=requests.get(o,headers=headers,timeout=30).text
            html2=etree.HTML(kaishi)
            try:
                img=html2.xpath('//div[@class="text"]/p/text()')[0]
            except:
                img=""
                print (o)
            if  (u"图" not  in img)and(u"以上" not  in img)and(u"上面" not  in img) :
                title=html2.xpath('//div[@class="title"]/h1/text()')
                test_cs=html2.xpath('//div[@class="qList"]/div[@class="item"]')

                for  t  in test_cs:

                    test=t.xpath('div[@class="t"]/text()')
                    cs_answer = t.xpath('div[@class="c"]/div[@class="radio"]/label/text()')
                    # t = (reduce(lambda x, y: str(x+",").strip()+ str(y).strip(), cs_answer))
                    if len(cs_answer)>=4 :
                        try:
                            d1 = t.xpath('div[@class="c"]/div[@class="radio"][1]/label/text()')[0].strip()
                            d1=re.sub("[A-Z.]|：|、| ","",d1)
                        except:
                            print("答案1出错")
                        try:
                            d2 = t.xpath('div[@class="c"]/div[@class="radio"][2]/label/text()')[0].strip()
                            d2 = re.sub("[A-Z.]|：|、| ", "", d2)
                        except:
                            print("答案2出错")
                        try:
                            d3 = t.xpath('div[@class="c"]/div[@class="radio"][3]/label/text()')[0].strip()
                            d3 = re.sub("[A-Z.]|：|、| ", "", d3)
                        except:
                            print("答案3出错")
                        try:
                            d4 = t.xpath('div[@class="c"]/div[@class="radio"][4]/label/text()')[0].strip()
                            d4 = re.sub("[A-Z.]|：|、| ", "", d4)
                        except:
                            print("答案4出错")
                        try:
                            d5 = t.xpath('div[@class="c"]/div[@class="radio"][5]/label/text()')[0].strip()
                            d5 = re.sub("[A-Z.]|：|、| ", "", d5)
                        except:
                            d5=''
                            print("没有5个答案")
                        if '\u4e00' <= d1 <= '\u9fff':
                            answer_list.append((title[0],test[0],d1,d2,d3,d4,d5,o))
                            print (d1,d2,d3,d4,d5,o)
    return answer_list

#
def baocu(ls):
    with open("test.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["标题", "测试题名", "答案1", "答案2", "答案3", "答案4", "答案5","url"])
        for r in ls:
            writer.writerow(r)




if __name__ == '__main__':
        c=ceshi()
        baocu(c)




