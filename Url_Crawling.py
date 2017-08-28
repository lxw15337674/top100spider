from bs4 import BeautifulSoup
import urllib.request


class spider(object):
    # todo 这个网页只有top10,后面的是index-2 到 index- 10.
    top_url = "http://www.mtime.com/top/movie/top100/"
    data = []
    num = 1

    def main(self):
        for a in range(2, 12):
            self.downloading()
            self.get_date()
            self.top_url = "http://www.mtime.com/top/movie/top100/index-%s.html" % a
        # print(self.data)
        self.out()

    # 爬取网页
    def downloading(self):
        # 伪装浏览器头
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
        req = urllib.request.Request(url=self.top_url, headers=header)
        html = urllib.request.urlopen(req).read()
        self.soup = BeautifulSoup(html, 'html.parser')

    # 爬取有用数据
    def get_date(self):
        if self.soup is None:
            raise Exception("获取不到爬取的网页")
        for item in self.soup.find_all('div', class_='mov_pic'):
            self.data.append(item.a['href'])
        print("成功爬取%s页" % self.num)
        self.num+=1
        # # 评分
        # for item in self.soup.find_all('div', class_='mov_point'):
        #     print(item.b.text)

    # 把url输出为txt
    def out(self):
        with open('top_url.txt', 'w', encoding='utf-8') as f:
            for i in self.data:
                f.write(i + "\n")


if __name__ == '__main__':
    spider = spider()
    spider.main()
