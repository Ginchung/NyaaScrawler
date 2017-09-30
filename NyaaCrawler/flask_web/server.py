# hello.py
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import requests
import base64

from NyaaCrawler.flask_web.model import ArticleList
from NyaaCrawler.flask_web.ImageParse.ImageHandler import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("table.html",
      title='Flask Bootstrap Table')

# 回傳文章資料json格式
@app.route('/post', methods=['GET', 'POST'])
def post():
    query = {}
    query["offset"] = request.args.get('offset')
    query["order"] = request.args.get('order')
    query["sort"] = request.args.get('sort')
    query["limit"] = request.args.get('limit')
    query["keyword"] = request.args.get('keyword')
    query["fromDate"] = request.args.get('fromDate')
    query["toDate"] = request.args.get('toDate')
    query["minSize"] = request.args.get('minSize')
    query["maxSize"] = request.args.get('maxSize')
    query["maxage"] = request.args.get('maxage')


    al = ArticleList()
    items = al.GetArticleByKey(**query)
    pagination = {'total': items.get("total")}
    pagination['rows'] = list(items.get("article"))
    return jsonify(pagination)

# 取得預覽圖連結的陣列 回傳預覽圖片連結的陣列
@app.route('/getImage', methods=['GET', 'POST'])
def getImage():
    imgs = []
    data = request.get_json()
    print('server.py getImage() data=',data)
    ImagePath = data['ImagePath']

    # 宣告圖片陣列 用來防止重覆圖片
    imgList = []

    for item in ImagePath:
        url = item['url']
        domain = item['domain']
        img = Image(domain, url)
        # 取得圖片連結
        imgPath = img.get()

        if imgPath and imgPath not in imgList:
            imgList.append(imgPath)
            # 將圖片轉成base64
            response = requests.get(imgPath)
            imgBase64 = ("data:" +
                   response.headers['Content-Type'] + ";" +
                   "base64," + str(base64.b64encode(response.content),'utf8'))

            imgs.append(imgBase64)
    # 回傳base64格式的字串
    return jsonify(imgs)

if __name__=='__main__':
    app.run(debug=True)