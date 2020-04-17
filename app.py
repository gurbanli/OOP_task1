from flask import Flask, render_template, request, redirect, url_for
from forms import AreaForm
from secrets import token_urlsafe
from area import ParquetFloor, WoodenFloor
from master import Master

app = Flask(__name__)
app.config['SECRET_KEY'] = token_urlsafe(16)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AreaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            width = form.width.data
            height = form.height.data
            color = form.color.data
            material = form.material.data
            num_of_masters = form.num_of_masters.data
            area = int(width) * int(height)
            price = get_results(width, height, color, material, num_of_masters)
            return redirect(url_for('show_results', price=price, area=area))
        else:
            return redirect('/')

    return render_template('index.html', form=form)


def get_results(width, height, color, material, num_of_masters):
    if material == 'parquet':
        floor = ParquetFloor(width, height, color)
        master = Master(num_of_masters)
        return floor.price() + master.price_of_masters
    elif material == 'wooden':
        floor = WoodenFloor(width, height, color)
        master = Master(num_of_masters)
        return floor.price() + master.price_of_masters


@app.route('/result', methods=['GET'])
def show_results():
    price = request.args['price']
    area = request.args['area']
    return render_template('result.html', price=price, area=area)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
