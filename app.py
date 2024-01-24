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
def execute_query(conn,query,args=None):
    with conn.cursor() as cursor:
        cursor.execute(query,args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:   
            conn.commit()   

@app.route('/',methods=("GET",))
def index():
	per_page = 20
	page,_,offset = get_page_args(per_page=per_page)
	# 카테고리 name 가져오기
	category = request.args.get('category')
	# 검색 name 가져오기
	search_q = request.args.get('q')
	sql = "SELECT count(*) as sum FROM kream"
	cur.execute(sql)
	sum = cur.fetchone()
	sum = int(sum['sum'])

	sql = "SELECT * FROM kream LIMIT %s OFFSET %s"
	# sql = "SELECT * FROM kream LIMIT %s OFFSET %s"
	cur.execute(sql,(per_page,offset))
	kream_data = cur.fetchall()
	kream_data_len = len(kream_data)
	pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True) 
	
    # 카테고리 선택 기능
	if category=="상의":
		# 검색 기능 카테고리 : 상의 에서 제품 검색
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		#카테고리 상의 검색
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
			
	elif category=="하의":
		
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="신발":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="패션잡화":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="아우터":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="가방":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="지갑":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="시계":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="컬렉터블":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="뷰티":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="테그":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="캠핑":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="가구/리빙":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])
			
			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
		else:
			sql = "SELECT count(*) as sum FROM kream WHERE category=%s"
			cur.execute(sql,(category))
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = "SELECT * FROM kream WHERE category=%s LIMIT %s OFFSET %s"
			cur.execute(sql,(category,per_page,offset))
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)
	elif category=="전체":
		if search_q:
			sql = f"SELECT count(*) as sum FROM kream WHERE product_name LIKE '%{search_q}%' and category = '{category}'"
			cur.execute(sql)
			sum = cur.fetchone()
			sum = int(sum['sum'])

			sql = f"SELECT * FROM kream WHERE product_name LIKE '%{search_q}%'"
			cur.execute(sql)
			kream_data = cur.fetchall()
			kream_data_len = len(kream_data)
			pagination=Pagination(page=page,total=sum,per_page=per_page,prev_label="Previous",next_label="Next",format_total=True)

	return render_template('indext.html',kream_data = kream_data,kream_data_len=kream_data_len,pagination=pagination,search=True,bs_version=5)



@app.route('/delete',methods=("POST",))
def delete():
	ids = request.form['ids']
	ids = ids.split(",")[0:-1]
	print(ids)
	for id in ids:
		sql = f'DELETE FROM kream WHERE ID={id}'
		cur.execute(sql)
		db.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)