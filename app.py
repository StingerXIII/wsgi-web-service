def application(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    request_method = env['REQUEST_METHOD']
    if request_method == 'GET':
        response_body = 'received GET request'
    elif request_method == 'POST':
        response_body = 'received POST request'
    else:
        response_body = 'request method is not implemented'
    return response_body