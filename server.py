from flask import Flask, request


"""
Ziphon is code name for tuition_server project
"""
class Ziphon:
	__app = Flask("Ziphon",static_folder='public', static_url_path='')

	@__app.route("/")
	def hello():
    		return "Hello World!"

	def start(self):
		self.__app.run(debug=True, host='localhost', port=4545)

if __name__ == "__main__":
	ziphon = Ziphon()
	ziphon.start()
