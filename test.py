from bs4 import BeautifulSoup
import urllib.request


class spider(object):
    soup = ''
    urls = ["http://movie.mtime.com/12428/"]
    rank = 0


    def pagemain(self):
        count = 1
        for url in self.urls:
            self.downloading(url=url)
            self.get_date()
            self.out(url=url)
            print("已成功爬取%s个,电影名:%s" % (count,self.movie_name ))
            count += 1

    # 爬取网页
    def downloading(self, url):
        # 伪装浏览器头
        header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.0.0.3"}
        req = urllib.request.Request(url=url, headers=header)
        html = urllib.request.urlopen(req).read()
        self.soup = BeautifulSoup(html, 'html.parser')

    # 爬取有用数据
    def get_date(self):
        if self.soup is None:
            raise Exception("获取不到爬取的网页")

        # 排名
        self.rank += 1

        # 电影名
        self.movie_name = self.soup.find('h1', style="font-size:35px;").text

        # 评分 评分在这个页面应该为动态加载的,无法爬取.所以只能暂时通过在热榜中爬取

        # 英文名
        self.movie_enname = self.soup.find('p', class_="db_enname").text

        # 上映年份
        self.movie_year = self.soup.find('p', class_="db_year").text

        # 时长
        self.movie_runtime = self.soup.find('div', class_='otherbox __r_c_').span.text

        # 类型
        movie_genre = ""
        for genre in self.soup.find_all('a', property='v:genre'):
            movie_genre += genre.text + ","
        # 去除最后的逗号
        self.movie_genre = movie_genre.strip(',')

        # 这里的电影标签特征一样,只能通过顺序分类
        box = self.soup.find('dl', class_="info_l").find_all('dd', class_='__r_c_')
        # 提取并进行数据清洗
        self.movie_dirctor = box[0].text[4:]
        self.movie_Screenwriter = box[1].text[4:].replace('\n', ',')
        self.movie_country = box[2].text[7:]
        self.movie_compang = box[3].text[7:-5]
        # 有可能电影没有别名
        try:
            self.movie_othername = box[4].text[7:-5].replace('\n', ',')
        except:
            self.movie_othername = ""

    def out(self, url):
        with open('data.txt', 'w', encoding='utf-8') as f:
            # f.write("排名#电影名#评分#英文名#别名#上映时间#时长#类型#导演#编剧#制作国家#发行公司#url\n", )
            # f.write("%s#%s#%s#%s#%s#%s#%s#%s#%s#%s#%s#%s#%s\n"
            f.write("%s %s %s %s %s %s %s %s %s %s %s %s \n"
                    % (self.rank, self.movie_name,
                    #todo 评分暂空
                       " ",
                       self.movie_enname,
                    self.movie_othername,self.movie_year,
                    self.movie_runtime,self.movie_genre,
                    self.movie_dirctor, self.movie_Screenwriter,
                    self.movie_country,self.movie_compang,
                    # url
                       ))


if __name__ == '__main__':
    spider = spider()
    spider.pagemain()
