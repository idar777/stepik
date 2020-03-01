def hello(environ, start_response): # бизнес-логика
   status = '200 OK'
   headers = [('Content-Type', 'text/plain') ]
   getParam = environ['QUERY_STRING'].replace('&', '\n')
   body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
   start_response(status, headers)
   return body
