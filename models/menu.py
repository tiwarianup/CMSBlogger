# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

response.logo = A(B('BLOGGER'),XML('&nbsp;'),
                  _class="brand",_href="/Blog/default/index")
response.title = ''
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Anup Tiwari - anup.tiwari39.gmail.com'
response.meta.keywords = 'CMS Multiple Blogs'
response.meta.generator = ''

## your http://google.com/analytics id
response.google_analytics_id = None

response.menu = [
    (T('HOME'), False, URL('default', 'index')),
    (T('BLOGS'), False, URL('default', 'home')),
    (T('CREATE BLOG'), False, URL('default', 'create_blog')),
    (T('ANALYSIS'), False, URL('analysis', 'index'))
]

if auth.has_membership('members'):
	response.menu.append((T('MANAGE'), False, URL('default', 'manage_post')))

if "auth" in locals(): auth.wikimenu()
