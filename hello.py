def hello(environ, start_response): # бизнес-логика
   status = '200 OK'
   headers = [('Content-Type', 'text/plain') ]
   getParam = environ['QUERY_STRING'].replace('&', '\n')
   start_response(status, headers)
   return [ getParam ]
