from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!
    # 클라이언트가 준 수량 이름 주소 전화번호 가져오기
    order_name_receive = request.form['order_name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    # db에 정보 삽입
    db.myshop.insert_one({
        'name': order_name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    })

    # 성공여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문완료'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.myshop.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
