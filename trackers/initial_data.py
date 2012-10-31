#
# TRACKER INITIAL PRIORITY AND STATUS VALUES
#
pri = db.getclass('priority')
pri.create(name=''"low", order="1")
pri.create(name=''"normal", order="2")
pri.create(name=''"high", order="3")
pri.create(name=''"emergency", order="4")

stat = db.getclass('status')
stat.create(name=''"unread", order="1")
stat.create(name=''"deferred", order="2")
stat.create(name=''"moreinfo", order="3")
stat.create(name=''"policyreview", order="4")
stat.create(name=''"in-progress", order="5")
stat.create(name=''"testing", order="6")
stat.create(name=''"resolved", order="7")

# create the two default users
user = db.getclass('user')
user.create(username="admin", password=adminpw,
    address=admin_email, roles='Admin')
user.create(username="anonymous", roles='Anonymous')

# default departments
department = db.getclass('department')
department.create(name=''"building", order="1")
department.create(name=''"isawit", order="2")
department.create(name=''"research", order="3")
