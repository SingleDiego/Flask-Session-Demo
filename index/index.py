from flask import (
    Flask, 
    url_for, 
    render_template,
    request,
    make_response,
    session,
    abort, # 放弃请求并返回错误代码
    redirect, # 重定向
    )
from werkzeug import secure_filename


app = Flask(__name__)

# 设置密钥，这段字符串请保密
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    # 如果 session 有 username 字段
    if 'username' in session:
        return 'User:' + session['username']
    # 如果 session 没有 username 字段
    return 'You are not logged in'


@app.route('/login', methods=['POST', 'GET'])
def login():
    #请求方法为 POST
    if request.method == 'POST':
        # 在 session 中添加 username 字段
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    # 请求方法为 GET
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # 删除 session 中当前用户的字段
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=3000,
        )