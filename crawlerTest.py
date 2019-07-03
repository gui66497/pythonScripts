import requests

# 移植于原java爬虫代码 包含rest接口请求 文件创建 远程文件下载 字符串处理等基本操作

# 获取远程接口数据
url = "http://bd.cstor.cn:8081/exp/listExp?title=&uid=2&pageSize=5&pageNumber=1"
headers = {'token': "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjEifQ.74Hq08NHOoLa6JvdGdKc7xYGzbmjROfBPqRHp5jOaAE"}
r = requests.get(url, headers=headers)
arr = r.json()["rows"]


# 替换图片路径并缓存图片到本地
def replace_img_url(text, save_type):
    if save_type == 1:
        pattern = "/static/upload/exp/"
        split_arr = text.split(pattern)
        if len(split_arr) > 0:
            real_str = ".\\images\\".join(split_arr)
            for s in split_arr:
                if ".png" in s and s.find("_") == 13:
                    image_name = s[0:s.find(".png") + 4]
                    download("http://bd.cstor.cn/static/upload/exp/" + image_name, image_name, "./html/images/")
            return real_str
        return text


# 文件下载
def download(file_url, file_name, path):
    result = requests.get(file_url)
    with open(path + file_name, "wb") as code:
        code.write(result.content)


for row in arr:
    # id = row["id"]
    html = "<html><header><link href=\".\\images\\main.css\" rel=\"stylesheet\"></header><body><div " \
           "class=\"NewPDF\"><div id=\"pdfDom\" class=\"NewPDF_C\"><div> "
    html += "<h1 class=\"Ntt1\">" + row["title"] + "</h1>"
    html += "<h2 class=\"Ntt2\">实验目的</h2>"
    html += "<div class=\"tContent lData\">"
    html += row["purpose"]
    html += "</div>"
    html += "<h2 class=\"Ntt2\">实验要求</h2>"
    html += "<div class=\"tContent \">"
    html += row["requirement"]
    html += "</div>"
    html += "<h2 class=\"Ntt2\">实验原理</h2>"
    html += "<div class=\"tContent \">"
    html += replace_img_url(row["principle"], 1)
    html += "</div>"

    html += "</div></div></div></body></html>"
    print(html)

    # 生成html文件
    htmlName = row["title"].replace("\r", "")
    file = open("./html/" + htmlName + ".html", 'w')
    file.write(html)
    file.close()

print(r.json)
