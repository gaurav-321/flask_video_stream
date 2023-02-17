import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='download')
app.config['SECRET_KEY'] = os.urandom(12).hex()


@app.route('/')
def all_route():
    return redirect("/index")


@app.route('/index')
def home():  # put application's code here
    data = [x for x in os.listdir("download")] * 10
    if request.args.get('search'):
        data = [x for x in data if request.args.get('search') in x]
    if len(data) > 0:
        chunks = [data[x:x + 12] for x in range(0, len(data), 12)]
    else:
        chunks = [[]]
    try:
        page = int(request.args.get('page'))
    except:
        page = 0
    return render_template("home.html", video_files=chunks[page], page=page, next_page=len(chunks) > page + 1)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True, use_reloader=True)
