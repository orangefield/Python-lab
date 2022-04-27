from flask import Flask
# Flask 경량 웹 프레임워크 : 파일 하나로 서버를 만들 수 있다!

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
