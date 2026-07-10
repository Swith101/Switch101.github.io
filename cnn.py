

#CNN RSS新闻源地址
RSS_URL="https://rss.cnn.com/rss/cnn_world.rss"
CSV_SAVE="cnn_news.csv"
JSON_SAVE="cnn_news.json"

# 获取单篇新闻完整正文
定义获取文章完整(URL)(_A)：
尝试:
标题={"用户代理"："Mozilla/5.0爬虫"}
res=请求.得到(URL，headers=headers，timeout=10)
汤=美丽的汤(res.文本，"html.parser")
段落=汤。 选择(".分段")
内容="\n".参与([p。获取文本(_T)(带=正确)为p在...内段落])
返回内容
除……之外：
返回 "正文获取失败"

#核心RSS抓取函数
定义fetch_cnn_rss()：
标题={
"用户代理"："Mozilla/5.0(Windows10)RSS爬虫个人使用"
    }
RESP=请求.得到(RSS_URL，headers=headers，timeout=18)
RESP.编码="utf-8"
root=ET.fromString(RESP.文本)
news_list=[]
为项在……内根。findall(".//channel/item")：
链接=项目。findtext("链接"，"")
新闻_项目={
"标题"：项。findtext("标题"，"")，
            "链接"：链接，
"摘要"：项。findtext("描述"，"")，
"全文(_T)"：get_article_full(链接)，
"发布时间(_T)"：项。findtext("pubDate"，"")，
"爬网时间"：datetime。现在().strftime("%Y-%m-%d%H：%M：%S")
        }
新闻列表(_L)。追加(新闻_项目)
返回新闻列表(_L)

#保存Excel可读的csv文件
定义save_csv(数据)：
如果 不数据：
        返回
keys=数据[0].键()
和……一起打开(CSV_SAVE，"w"，换行符=""，编码="utf-8-sig")作为f：
writer=csv.DictWriter(F，字段名称=关键字)
作家。WriteHeader()
作家。writerows（数字）

# 保存结构化json文件
定义save_json(数据)：
和……一起打开(JSON_SAVE，"w"，编码="utf-8")作为f：
JSON.倾倒(data，f，sure_ascii=假的，缩进=2)

# 程序启动入口
如果__名称__=="__主要的__"：
新闻=fetch_cnn_rss()
    如果新闻：
save_csv(新闻)
save_json(新闻)
打印(f"抓取完成，共获取{Len(新闻)}条CNN新闻")
    其他:
        打印("抓取失败，网络无法访问CNN")
