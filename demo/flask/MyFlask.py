from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("hllo.html")

@app.route("/")
def index():
    s = "你好啊,我是一个普普通通的网页"
    lst = ["长津湖", "长津湖", "长津湖"]
    return render_template("hllo.html", jay=s, lst=lst)



if __name__ == '__main__':
    app.run()