"""
2019年5月19日添加
爬取豆瓣热门评论的内容
使用最简单的requests+beautifulSoup
"""
import re
import time
import requests
from bs4 import BeautifulSoup


class SpiderReview():
    """爬取豆瓣热门评论所有缩略内容，存入文件中"""

    url = "https://book.douban.com/review/best/"
    params = {}
    reviews = []

    def writeReviews(self,text):
        """将评论内容写入txt文件中"""
        now = time.strftime("%y-%m-%d %X", time.localtime(time.time()))
        with open(now+"豆瓣评论.txt", 'w') as f:
            for iterm in text:
                f.write(iterm)
                f.write('\n\n')

    def getResponse(self, params):
        """爬取单页内容"""
        response = requests.get(self.url, params)
        soup = BeautifulSoup(response.text, "lxml")

        for iterm in soup.find_all('div', class_="short-content"):  # 获取标签类型为div，class属性为short-content的网页内容

            text = re.sub(r"<.*?>|这篇书评可能有关键情节透露|\s", "", str(iterm))  # 将标签 或者 "这篇书评可能有关键情节透露" 或者 空白区域 全部去掉
            self.reviews.append(str(text))

    def allReviews(self):
        """爬取所有的热门评论内容，总共50条，分3页。第一页start=0，第二页=20，第三页start=40"""
        for i in [0, 20, 40]:
            self.params['start'] = i
            self.getResponse(self.params)
        self.writeReviews(self.reviews)


if __name__ == '__main__':

    review = SpiderReview()
    review.allReviews()




