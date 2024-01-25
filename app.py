from flask import Flask,render_template,request,redirect
from flask_paginate import Pagination, get_page_args

import pymysql
app = Flask(__name__)
db = pymysql.connect(
	host = 'localhost',
    user='root',
    password = '0000',
    db='kream',
    charset = 'utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)
cur = db.cursor()

# 페이지네이션 total 갯수 구하는 execute 함수
def first_execute(args):
	cur.execute(args)
	sum = cur.fetchone()
	sum = int(sum['sum'])
	return sum

@app.route('/',methods=("GET",))
def index():
	per_page = 20
	page,_,offset = get_page_args(per_page=per_page)
	# 카테고리 name 가져오기
	category = request.args.get('category')
	# 검색 name 가져오기
	search_q = request.args.get('q')

	# 전체 카테고리 빼고 모드 카테고리 검색
	if category and category!="전체":
		#카테고리 선택후 제품명 검색 코드
		if search_q:
			sql1 = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			sum = first_execute(sql1)

			sql2 = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}' LIMIT {per_page} OFFSET {offset}"
			cur.execute(sql2)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		#카테고리 검색 코드
		else:
			sql1 = f"SELECT count(*) as sum FROM kream WHERE category='{category}'"
			sum = first_execute(sql1)

			sql2 = f"SELECT * FROM kream WHERE category='{category}' LIMIT {per_page} OFFSET {offset}"
			cur.execute(sql2)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	#전체 카테고리 따로 검색
	elif category=="전체":
		if search_q:
			sql1 = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%'"
			sum = first_execute(sql1)

			sql2 = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' LIMIT {per_page} OFFSET {offset}"
			cur.execute(sql2)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
			#카테고리 상의 검색
		else:
			print("a")
			sql1 = "SELECT count(*) as sum FROM kream"
			sum = first_execute(sql1)

			sql2 = f"SELECT * FROM kream LIMIT {per_page} OFFSET{offset}"
			cur.execute(sql2)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	#처음 페이지 시작
	else:
		sql1 = "SELECT count(*) as sum FROM kream"
		sum = first_execute(sql1)

		sql2 = f"SELECT * FROM kream LIMIT {per_page} OFFSET {offset}"
		# sql = "SELECT * FROM kream LIMIT %s OFFSET %s"
		cur.execute(sql2)
		kream_data = cur.fetchall()
		kream_data_len = len(kream_data)
		pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		 
	return render_template('indext.html',kream_data = kream_data,kream_data_len=kream_data_len,pagination=pagination,search=True,bs_version=5)


@app.route('/delete',methods=("POST",))
def delete():
	ids = request.form['ids']
	ids = ids.split(",")[0:-1]
	for id in ids:
		sql = f'DELETE FROM kream WHERE ID={id}'
		cur.execute(sql)
		db.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)