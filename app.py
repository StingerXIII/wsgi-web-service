
def application(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    request_method = env['REQUEST_METHOD']
    request_body = env['wsgi.input'].read()
    if request_method == 'GET':
        response_body = 'received GET request\n'
        if env['PATH_INFO'] == '/last':
            response_body = response_body + get_last_record()
    elif request_method == 'POST':
        response_body = 'received POST request\n' + 'request body is:\n' + request_body
    else:
        response_body = 'request method is not implemented\n'
    return response_body


def get_last_record():
    pass
