def application(env, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    response_body = process_request(env['REQUEST_METHOD'],'')
    return repr(response_body)



def process_request(request_method, request_body):
    response_body = []
    if request_method == 'GET':
        response_body.append('received GET request')
    elif request_method == 'POST':
        response_body.append('received POST request')
    else:
        response_body.append('request method is not implemented')
    return response_body