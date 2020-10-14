from flask import Flask, render_template, url_for, request, redirect
from forms import BissectionForm
from Numeric_method import functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'

@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def index():
    form = BissectionForm()

    if request.method == 'POST' and form.validate_on_submit():
        a = form.down_limit.data
        b = form.upper_limit.data
        tol = form.precision.data
        
        k_value = functions.k_estimated(a, b, tol)
        bissection_value = functions.bissection_method(a, b, tol)
    
        data_dict = {
            'k_estimated': int(k_value),
            'root': bissection_value['root'],
            'n_iterations': bissection_value['k']
        }
        return render_template('result.html', results=data_dict)
   
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=False)