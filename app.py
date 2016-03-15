def application(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    request_method = env['REQUEST_METHOD']
    if request_method == 'GET':
        response_body = 'received GET request\n'
    elif request_method == 'POST':
        response_body = 'received POST request\n'
    else:
        response_body = 'request method is not implemented\n'
    return response_body