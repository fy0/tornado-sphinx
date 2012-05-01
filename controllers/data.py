
# coding:utf-8

import tornado.web

import controllers.usesql as us
import controllers.sphinx as sphinx

class search(tornado.web.RequestHandler):
    def get(self):
        try:
            key = self.get_argument('key')
        except:
            return self.redirect('/')
        ret = sphinx.query(key)

        if not ret:
            print '未找到'
        else:
            search_info = '获得 %d 个结果从 %d 个匹配项，耗时 %s sec' % ( ret['total'], ret['total_found'], ret['time'])
            #for info in ret['words']:
		    #    print '%s 共找到 %d 次，在 %d 个文档中' % (info['word'], info['hits'], info['docs'])
            _data = []
            for match in ret['matches']:
                _r = us.getDataById(match['id'])
                # title,url
                _data.append([_r[0][2],_r[0][1]])
            #print('doc_id=%s, 权重=%d' % (match['id'], match['weight']))
        self.render('search.html',search_info=search_info,mathes=ret['matches'],items=_data,key=key)
    def post(self):
        try:
            key = self.get_argument('key')
        except:
            return self.redirect('/')
        self.redirect('/search?key=%s'%key)

