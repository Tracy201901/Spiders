"""
爬取微博主页正文，存入csv文件中
返回数据类型为json
"""
# _*_ coding:utf-8 _*_
import re
import requests
import csv
import time
import  random

class GetAllTexts():
    '''获取所有的微博数据'''
    url =  "https://m.weibo.cn/api/container/getIndex"
    params = {'display': '0','retcode': '6102', 'type': 'uid','value': '1902523877', 'containerid': '1076031902523877'}
    headers = {'Accept': 'application/json;charset=utf-8','User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1;zh-cn; XT1085/LPES23.32-70-5) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.1 Mobile Safari/537.36', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'com.lenovo.browser','Connection': 'keep-alive'}
    title = ['微博发布时间', '微博mid', '此条微博评论数', '微博正文','转发微博创建时间','转发微博mid','转发微博正文','转发微博作者']

    def write_csv(self, text_list):
        weibo_text = text_list
        title = self.title
        print('开始写入文件')
        with open('八月徐子善所有微博正文.csv', 'w+',encoding='utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            spamwriter.writerow(title)
            for l in weibo_text:
                spamwriter.writerow(l)

    def get_page(self, page_id):
        url = self.url
        params = self.params
        params['page'] = page_id
        headers = self.headers
        try:
            r = requests.get(url=url, params=params, headers=headers)
            print(r.url)
            time.sleep(random.randint(1,5))
            j = r.json()
            data = j.get('data')
            cardlistInfo = data.get('cardlistInfo')
            page = cardlistInfo.get('page')  # 服务器返回下一页数据页码
            cards = data.get('cards')  # 每一条微博是一个单独的card，所有card组成一个列表
            return page,cards
        except:
            return 'end',[]

    def clean_text(self,weibo_text):
        dirt_text = weibo_text
        p = re.compile('<[^>]+>')
        clean_text = p.sub('',dirt_text)
        return clean_text

    def get_info_from_single_card(self,card):
        """把微博card中的内容存入list中"""
        card_info = []
        try:
            #原创微博和转发微博共有部分
            mblog = card.get('mblog')
            card_info.append(mblog.get('created_at'))  # 添加表格第1列：创建微博的时间
            card_info.append(mblog.get('mid')) # 添加表格第2列：微博mid
            card_info.append(mblog.get('comments_count')) # 添加表格第3列：评论数量
            text1 = mblog.get('text')
            new_text1 = self.clean_text(text1)
            card_info.append(new_text1) # 添加表格第4列：微博正文

            #判断微博是否有转发内容，有转发内容就加上：
            retweeted_status = mblog.get('retweeted_status')
            if retweeted_status != None:
                retweeted_status = mblog.get('retweeted_status')
                card_info.append(retweeted_status.get('created_at'))# 添加表格第5列：转发微博创建时间
                card_info.append(retweeted_status.get('mid'))# 添加表格第6列：转发微博mid
                text2 = retweeted_status.get('text')
                new_text2 = self.clean_text(text2)
                card_info.append(new_text2)# 添加表格第7列：转发微博正文内容
                user = retweeted_status.get('user')
                card_info.append(user.get('screen_name'))# 添加表格第9列：转发微博创建时间
            else:
                card_info.append('无')
                card_info.append('无')
                card_info.append('无')
                card_info.append('无')
            return card_info
        except:
            return ['获取card内容失败']

    def get_all_cards_info(self, cards):
        """获取整页数据所有card的内容存放于text_list中"""
        text_list = []
        for card in cards:
            if card.get('card_type') == 11: #类型为11的card没有有效内容，跳过
                continue
            else:
                single_card = self.get_info_from_single_card(card)
                print('微博内容:',single_card,'\n')
                text_list.append(single_card)
        return text_list

    def get_all_text(self):
        """获取博主所有历史微博数据，存放于csv文件中"""
        page_id = ''
        all_text = []
        while True:
            page_id,cards = self.get_page(page_id)
            if len(cards) == 0:
                break
            else:
                one_page_text = self.get_all_cards_info(cards)
                for iterm in one_page_text:
                    all_text.append(iterm)
            if page_id == None:
            #if page_id == 4:
                break
        self.write_csv(all_text)


if __name__ == '__main__':

    all_page = GetAllTexts()
    all_page.get_all_text()

