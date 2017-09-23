# hello.py
from flask import Flask
from flask import render_template
from bson.json_util import dumps, loads
from NyaaCrawler.flask_web.model import ArticleList
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    # 取得所有資料
    items = ArticleList().GetArticleAll().get("article")
    # items = [doc for doc in items]
    return render_template("table.html",
      title='Flask Bootstrap Table')

# 回傳文章資料json格式
@app.route('/get', methods=['GET', 'POST'])
def get():
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


if __name__=='__main__':
    app.run(debug=True)