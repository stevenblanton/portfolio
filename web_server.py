import csv
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
print(__name__)


def write_to_file(data):
    with open('./Web_Development/database.txt', mode='a', ) as file_append:
        file_append.write(
            f"\n{data['email']}, {data['subject']}, {data['name']}, {data['message']}")


def write_to_csv(data):
    with open('./Web_Development/database.csv', newline='', mode='a', ) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'],
                             data['name'], data['message']])


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            if request.form['email'] and request.form['name'] and request.form['message']:
                data = request.form.to_dict()
                write_to_csv(data)
                return render_template('/thankyou.html', name=data['name'])
            else:
                error = 'Need to fill all form fields!'
        except:
            return 'Record was not saved to database'
    else:
        return 'Something went wrong, try again!'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('contact.html', error=error)


# @app.route('/<username>/<int:post_id>')
# def username(username='User', post_id=0):
#     return render_template('username.html', name=username, post_id=post_id)


@app.route('/favicon.ico')
def favicon():
    app.add_url_rule('/assets/favicon.ico',
                     redirect_to='static/assets/favicon.ico')
