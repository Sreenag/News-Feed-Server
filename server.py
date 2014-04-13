from flask import Flask, request



class News:
	__app = Flask("Ziphon",static_folder='public', static_url_path='')

	@__app.route("/")
	def hello():
    		return "Hello world"

	def start(self):
		self.__app.run(debug=True, host='localhost', port=4545)

if __name__ == "__main__":
	news = News()
	news.start()
