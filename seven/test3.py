def appilcation(envision,start_response):
    start_response('200 0K',[('Content-Type','text-html')])
    boby = '<h1>Hello,%s!</h1>' % (envision['PATH_INFO'][1:] or 'web')
    return [boby.encode('utf-8')]
