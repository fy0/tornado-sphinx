# coding:utf-8

import tornado.web

from controllers import form,data

application = tornado.web.Application([
    # 访问模板
    (r"/",                 form.index),
    (r"/search",           data.search)
    ],

    template_path='templates',
    static_path='static',
    debug=True,
    cookie_secret="6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CC"
)

