# coding: utf8

#Table for New Blog title
db.define_table('blog_name',
				Field('title', requires = IS_NOT_EMPTY()),				
				auth.signature)


#Table for Post body
db.define_table('blog_post',
				Field('blog_name', 'reference blog_name', readable = False, writable= False, ondelete = 'NO ACTION'),
                Field('title', requires = IS_NOT_EMPTY()),
                Field('body', 'text', requires = IS_NOT_EMPTY()),
                auth.signature)

# Table for Comments
db.define_table('blog_comment',
                Field('blog_post', 'reference blog_post', ondelete = 'NO ACTION'),
                Field('body', requires = IS_NOT_EMPTY()),
                auth.signature)

db.define_table('tMISData', 
				Field('AppInstanceID'),
				Field('JobID', 'integer'),
				Field('DataFetchDate', 'datetime'),
				Field('Activity',),
				Field('BaseDate', 'datetime'),
				Field('BaseRef'),
				Field('Aging'),
				Field('Qty', 'integer'),
				Field('RequestDate', 'datetime'),
				Field('PostDate', 'datetime'),
				migrate = False)