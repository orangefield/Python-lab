# python -m pip install flask

from flask import Flask, request, jsonify
# Body 데이터 받을 때 request
# dict을 json으로 바꿀 때 jsonify
import member_dao as dao


flask = Flask(__name__)  # __main__


@flask.route("/my-member")  # Controller
def list():
    return jsonify(dao.select_all())


@flask.route("/my-member/<id>")
def detail(id):  # pathVariable
    return jsonify(dao.select_one(id=id))  # **data를 받고 있으니 id=id


@flask.route("/my-member/<id>", methods=["DELETE"])  # GET은 Default
def delete(id):
    return jsonify(dao.delete_one(id=id))


@flask.route("/my-member/<id>", methods=["PUT"])
def update(id):
    # data = request.data()  # 바디 데이터 받는 방법(x-www-form-urlencoded)
    data = request.get_json()  # application/json
    # print(data)
    return jsonify(dao.update_one(id=id, username=data["username"], password=data["password"]))
    # dict 타입은 key값


@flask.route("/my-member", methods=["POST"])
def save():
    data = request.get_json()
    # print(data)
    return jsonify(dao.insert_one(id=id, username=data["username"], password=data["password"]))


flask.run(  # 서버 실행
    host="0.0.0.0",  # 모든 IP에서 접근 가능
    port=5000,
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 reload
)
