from flask import Flask, jsonify
import psycopg2
from flask import request



app = Flask(__name__)



@app.route('/get_data',methods=['GET'])
def get_data():
    try:
        count =int(request.args.get('count'))
        sort_order=str(request.args.get('sort_order'))
        connection= psycopg2.connect(user="postgres",password="postgres",host='127.0.0.1', port='5432', database="imdb_data")
        cursor=connection.cursor()
        cursor.execute("SELECT TEXT , lable_number FROM data_input INNER JOIN data_labeling on id = text_id ORDER BY date_input %s LIMIT %s",[sort_order,count])
        result=cursor.fetchall()
        return  jsonify(result)
    except:
        return "Error"




@app.route('/get_data_count',methods=['GET'])
def get_data_count():
    try:

        count=int(request.args.get('count'))
        label=str(request.args.get('label'))
        if (label == 'positive'):
            lable_name = 1
        elif (lable == 'negative'):
              lable_name = 0
        connection= psycopg2.connect(user="postgres",password="postgres",host='127.0.0.1', port='5432', database="imdb_data")
        cursor=connection.cursor()
        cursor.execute("SELECT text_id, lable_number FROM data_labeling WHERE lable_number=1 fetch first 1000 rows only")
        result=cursor.fetchall()
        return jsonify(len(result))
    except:
        return "Error"


if __name__ == '__main__':
        app.run(debug=True, port=3000)
