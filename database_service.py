
from flask import Flask, jsonify
import psycopg2
from flask import request



app = Flask(__name__)




@app.route('/get_data_count',methods=['GET'])
def get_data_count():
    try:
        label_name=int(request.args.get('label_name'))
        count=int(request.args.get('count'))
        connection= psycopg2.connect(user="postgres",password="postgres",host='127.0.0.1', port='5432', database="imdb_data")
        cursor=connection.cursor()
        cursor.execute("SELECT COUNT(lable_name) FROM data_labeling WHERE lable_name = 1 ")
        result=cursor.fetchone()
        return  jsonify(result)
    except:
        return "Error"


@app.route('/get_data',methods=['GET'])
def get_data():
    try:
        count =int(request.args.get('count'))
        sort_order=str(request.args.get('sort_order'))
        connection= psycopg2.connect(user="postgres",password="postgres",host='127.0.0.1', port='5432', database="imdb_data")
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM data_input WHERE id < 5")
        result=cursor.fetchone()
        return  jsonify(result)
    except:
        return "Error"



if __name__ == '__main__':
    app.run(debug=True, port=3000)
