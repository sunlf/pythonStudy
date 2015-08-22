
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8000,help = "run on the give port",type=int)

class IndexHanler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html",page_title="Free IT Books",content_text="Hello Content",foot_text="Hello Foot")

class BookModule(tornado.web.UIModule):
	def render(self,book):
		return self.render_string("modules/book.html",book=book)

class RecommendedHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("recommended.html",page_title="recommended reading Books",books=[{
				"title":"CLR VIA C# 4",
				"image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif",
				"date_added":1310248056
			},
			{
				"title":"Thinking in java",
				"image":"https://www.baidu.com/img/baidu_jgylogo3.gif?v=39973032.gif",
				"date_added":1310248056
			}
			])


class BookStoreApp(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/',IndexHanler),
			(r'/reco',RecommendedHandler),
		]
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__),"templates"),
			static_path = os.path.join(os.path.dirname(__file__),"static"),
			ui_modules = {"Book":BookModule},
			debug=True
		)
		super().__init__(handlers,**settings)

if __name__ =='__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(BookStoreApp())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()