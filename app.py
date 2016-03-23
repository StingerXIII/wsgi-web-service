from app_config import db_parms
import psycopg2
import simplejson
import datetime


# db_parms syntax:
# db_parms = {
#     'db_name': '',
#     'login': '',
#     'password':  '',
#     'host': '',
#     'port': ''
# }

def application(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    request_method = env['REQUEST_METHOD']
    request_body = env['wsgi.input'].read()
    if request_method == 'GET':
        response_body = 'received GET request\n'
        if env['PATH_INFO'] == '/last':
            response_body += get_last_record()
    elif request_method == 'POST':
        response_body = 'received POST request\n' + 'request body is:\n' + request_body
    else:
        response_body = 'request method is not implemented\n'
    return response_body


def get_last_record():
    message = []
    query = """select rec_date, rec_time, rec_text from records
    where rec_date = (select max(rec_date) from records)
    and rec_time = (select max(rec_time) from records)"""
    conn = psycopg2.connect("dbname="+db_parms.get('db_name')+
                            " user="+db_parms.get('login')+
                            " host="+db_parms.get('host')+
                            " password="+db_parms.get('password'))
    cur=conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        record = {
            'res_date': row[0].strftime("%Y-%m-%d"),
            'res_time': row[1].strftime("%H:%M:%S"),
            'res_text': row[2]
        }
        message.append(record)

    return simplejson.dumps(message)

