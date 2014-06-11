# Test for da|ra API
# hendrik bunke <h.bunke@zbw.eu>, 11.06.2014

#import poster
import urllib2
import requests

def upload():

    # zur Einbindung der POST Parameter:
    # http://atlee.ca/software/poster/poster.encode.html#poster.encode.MultipartParam
    # simply passing a sequence (list with tuples (see 'fields') does NOT
    # work. Don't ask me why ;-)
    
    URL = 'http://dara-test.gesis.org:8084/dara/study/importXML'
    dara_login = 'demo'
    dara_pass = 'testdemo'
    xml = '/home/bunke/dev/ckanext-dara/ckanext/dara/dara_api/example_dataset.xml'
    filename = 'example_dataset.xml'

    files = {'file': open(xml, 'r')}
    
    #with open(xml, 'r') as stream:
    #    req = requests.post(URL, auth=(dara_login, dara_pass), data=stream)

    req = requests.post(URL, auth=(dara_login, dara_pass), files=files)
    http_code = req.status_code
    print http_code
    
    #import pdb; pdb.set_trace()
    #debug html output
    of = '/home/bunke/dop.html'
    #of = '/home/bunke/dop_files.html'
    #of = '/home/bunke/dop_stream.html'
    output = open(of, 'w')
    text = req.content
    output.write(text)
    output.close()
    print "output written to %s" %of


if __name__ == '__main__':
    print "starting upload..."
    r = upload()


