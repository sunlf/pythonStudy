
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

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
		books = self.application.db.books.find()
		self.render("recommended.html",page_title="recommended reading Books",books=books)

class BookEditHandler(tornado.web.RequestHandler):
	def get(self,isbn=None):
		book = dict()
		if isbn:
			coll = self.application.db.books
			book = coll.find_one({"isbn":isbn})
		self.render("bookedit.html",page_title="Edit Books",book=book)

	def post(self,isbn=None):
		import time
		book_field = ["isbn","title","image","date_released"]
		coll = self.application.db.books
		book = dict()
		if isbn:
			book = coll.find_one({"isbn":isbn})
		for key in book_field:
			book[key] = self.get_argument(key,None)

		if isbn:
			coll.save(book)
		else:
			book["date_added"] = int(time.time())
			coll.insert(book)
		self.redirect("/reco")


class BookStoreApp(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/',IndexHanler),
			(r'/reco',RecommendedHandler),
			(r'/edit/([0-9Xx\-]+)',BookEditHandler),
			(r'/add',BookEditHandler)
		]
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__),"templates"),
			static_path = os.path.join(os.path.dirname(__file__),"static"),
			ui_modules = {"Book":BookModule},
			debug=True
		)
		conn = pymongo.MongoClient("localhost",27017)
		self.db = conn.bookstore
		super().__init__(handlers,**settings)

if __name__ =='__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(BookStoreApp())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()