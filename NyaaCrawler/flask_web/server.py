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
@app.route('/get')
def get():
    offset = request.args.get('offset')
    order = request.args.get('order')
    limit = request.args.get('limit')
    al = ArticleList()
    items = al.GetArticleAll().get("article")
    pagination = {'total': al.GetAllDataCount()}
    pagination['rows'] = list(items)
    return jsonify(pagination)


if __name__=='__main__':
    app.run(debug=True)