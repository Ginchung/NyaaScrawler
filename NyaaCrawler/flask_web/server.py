# hello.py
from flask import Flask
from flask import render_template
from bson.json_util import dumps, loads
from NyaaCrawler.flask_web.model import ArticleList
app = Flask(__name__)


columns = [
  {
    "field": "title", # which is the field's name of data key
    "title": "標題", # display as the table header's name
    "sortable": True,
    "width":300
  },
  {
    "field": "torrent",
    "title": "種子",
    "sortable": True,
    "width": 300
  },
  {
    "field": "size",
    "title": "檔案大小",
    "sortable": True,
    "width": 300
  },
    {
        "field": "articlelink",
        "title": "文章連結",
        "sortable": True,
        "width": 300
    },
    {
        "field": "ImagePath",
        "title": "預覽圖連結",
        "sortable": True,
        "width": 100
    },
  {
    "field": "pubDate",
    "title": "發佈日期",
    "sortable": True,
    "width": 300
  }
]


@app.route('/')
def index():
    # 取得所有資料
    items = ArticleList().GetArticleAll().get("article")
    # items = [doc for doc in items]
    return render_template("table.html",
      data=list(items),
      columns=columns,
      title='Flask Bootstrap Table')

if __name__=='__main__':
    app.run(debug=True)