from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
  {
    'name': 'Shahab',
    'rollNo': 'i180731',
    'section': 'A',
    'title': 'post 1',
    'content': 'some random text'
  },
  {
    'name': 'Usama',
    'rollNo': 'i180616',
    'section': 'A',
    'title': 'new post',
    'content': 'another random text1'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', title='Store Managment System', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='AboutPage!!!')

if __name__ == "__main__":
    app.run(debug=True)