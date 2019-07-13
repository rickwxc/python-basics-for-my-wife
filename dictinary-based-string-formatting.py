
#access keys in dictnary easily
conf = {
        'url': 'http://localhost',
        'uri': '/hello-world/hi.html',
}
print ( '%(url)s%(uri)s' % conf)


def handle_comment(text):
    print("<!−−%(text)s−−>" % locals()) 

handle_comment('here is comments')


def tagWithDict(tag, attrsDict):
    strattrs = " ".join([' %s="%s"' % (key, value) for key, value in attrsDict.items()])
    print("<%(tag)s%(strattrs)s><%(tag)s>" % locals()) 

tagWithDict('div', {'width':100, 'height':200})


def tagWithLists(tag, attrsList):
    strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrsList])
    print("<%(tag)s%(strattrs)s>" % locals()) 

tagWithLists('div',  [('href', 'index.html'), ('title', 'Go to home page')])
