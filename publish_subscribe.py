#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Provider:

	def __init__(self):
		self.msg_queue = []
		self.subscribers = {}

	def notify(self,msg):
		self.msg_queue.append(msg)

	def  subscribe(self,msg,subscriber):
		if msg not in self.subscribers:
			self.subscribers[msg] = []
			self.subscribers[msg].append(subscriber)
		else:
			self.subscribers[msg].append(subscriber)


	def unsubscribe(self,msg,subscriber):
		self.subscribers[msg].remove(subscriber)


	def update(self):
		for msg in self.msg_queue:
			if msg in self.subscribers:
				for sub in self.subscribers[msg]:
					sub.run(msg)
		self.msg_queue = []


class Publisher:

	def __init__(self,msg_center):
		self.provider = msg_center

	def publish(self,msg):
		self.provider.notify(msg)

class Subscriber:

	def __init__(self,name,msg_center):
		self.name = name
		self.provider = msg_center

	def subscribe(self,msg):
		self.provider.subscribe(msg,self)

	def run(self,msg):
		print("{} got {}".format(self.name,msg))


def main ():
	msg_center = Provider()

	fftv = Publisher(msg_center)

	jim = Subscriber("jim",msg_center)
	jim.subscribe("cartoon")

	jack = Subscriber("jack",msg_center)
	jack.subscribe("music")

	gee = Subscriber("gee",msg_center)
	gee.subscribe("movie")

	fftv.publish("cartoon")
	fftv.publish("music")
	fftv.publish("ads")
	fftv.publish("movie")
	fftv.publish("cartoon")
	fftv.publish("cartoon")
	fftv.publish("cartoon")
	fftv.publish("blank")

	msg_center.update()


if __name__ == "__main__":
	main()

