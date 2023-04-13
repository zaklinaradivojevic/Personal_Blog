from flask import Flask, render_template, request, flash, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Add new post to database
        return 'Post added!'
    else:
        return render_template('new_post.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1320)
