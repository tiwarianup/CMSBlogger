# -*- coding: utf-8 -*-
import Quandl
import pygal
from pygal.style import CleanStyle  

#Homepage
def index():
    response.title = 'Welcome to Blogger CMS'
    return locals()

#Directory of all the available blogs
def home():
    response.title = 'Featured Blogs'
    blogs = db(db.blog_name).select(orderby = db.blog_name.id)
    return locals()

#Directory of all the available posts for a particular blog
def blog():
    response.title = 'Recent Posts'
    blog = db.blog_name(request.args(0, cast = int))
    blog_id = request.args(0, cast=int)
    posts = db(db.blog_post.blog_name == blog_id).select(orderby = db.blog_post.id)
    return locals()

def analytics():
    return locals()

def show_pie_chart():
    data = Quandl.get("BJS/ALC_CRIME", authtoken = "sDk4f2pSK3PSJqWRV177")
    response.headers['Content-Type'] = 'image/svg+xml'
    pie_chart = pygal.Pie(style=CleanStyle)
    pie_chart.title = 'Pie Chart of Different Assault Methods'
    pie_chart.add('Violent', data['Violent #'])
    pie_chart.add('Robbery', data['Robbery #'])
    pie_chart.add('Assault', data['Assault #'])
    pie_chart.add('Aggr Assault', data['Aggr Assault #'])
    pie_chart.add('Simple Assault', data['Simple Assault #'])
    return pie_chart.render()

def show_bar_chart():
    data = Quandl.get("BJS/ALC_CRIME", authtoken = "sDk4f2pSK3PSJqWRV177")
    bar_chart = pygal.Bar(style = CleanStyle)
    bar_chart.title = 'Bar Chart of Different Assault Methods'
    bar_chart.add('Violent', data['Violent #'])
    bar_chart.add('Robbery', data['Robbery #'])
    bar_chart.add('Assault', data['Assault #'])
    bar_chart.add('Aggr Assault', data['Aggr Assault #'])
    bar_chart.add('Simple Assault', data['Simple Assault #'])
    return bar_chart.render()

def show_radar_chart():
    data = Quandl.get("BJS/ALC_CRIME", authtoken = "sDk4f2pSK3PSJqWRV177")
    radar_chart = pygal.Radar(style = CleanStyle)
    radar_chart.title = 'Bar Chart of Different Assault Methods'
    radar_chart.add('Violent', data['Violent #'])
    radar_chart.add('Robbery', data['Robbery #'])
    radar_chart.add('Assault', data['Assault #'])
    radar_chart.add('Aggr Assault', data['Aggr Assault #'])
    radar_chart.add('Simple Assault', data['Simple Assault #'])
    return radar_chart.render()


#Form for creating a new blog
@auth.requires_login()
def create_blog():
    response.title = 'Create a new Blog'
    form = SQLFORM(db.blog_name).process()
    if form.accepted:
        session.flash = "Congratulations! New Blog Created"
        redirect(URL('home'))
    return locals()

#Page to show the full post and comments
# @auth.requires_login()
def display_post():
    post = db.blog_post(request.args(0, cast = int))
    db.blog_comment.blog_post.default = post.id
    db.blog_comment.blog_post.readable = False
    db.blog_comment.blog_post.writable = False
    form = SQLFORM(db.blog_comment).process()
    comments = db(db.blog_comment.blog_post == post.id).select()
    response.title = 'Full Article'
    return locals()

#Webpage interface to manage (view, edit, delete) posts and comments
@auth.requires_membership('members')
def manage_post():
    grid = SQLFORM.smartgrid(db.blog_post)
    response.title = 'Manage Posts'
    return locals()

#Form to create a new post
@auth.requires_login()
def create_post():
    response.title = 'Create New Blog Post'
    blog_name = db.blog_name(request.args(0, cast = int))
    db.blog_post.blog_name.default = blog_name
    form = SQLFORM(db.blog_post).process()
    if form.accepted:
        session.flash = "The content was successfully posted!"
        redirect(URL('blog', args = blog_name.id))
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
