from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import random

# ビルドされたHTMLファイルを読み込むための設定
app = Flask(__name__, static_folder="dist", static_url_path="")

# 開発時はあると便利。ビルドしたHTMLを使用するときには不要。
CORS(app)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# あとはフロント側からリクエストされる処理を好きに書く
@app.route("/message", methods=["POST"])
def get_message():
    message = random.choice(["Apple", "Banana", "Cherry"])
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
