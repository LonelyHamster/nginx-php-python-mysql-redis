from flask import Flask

# 创建一个 Flask 应用程序实例
app = Flask(__name__)

# 定义一个路由，指定 URL 路径和处理函数
@app.route('/')
def hello_world():
    return 'Hello, Python!'
