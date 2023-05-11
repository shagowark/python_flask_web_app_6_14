from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/task_1', methods=['GET', 'POST'])
def task_1():
    if request.method == 'GET':
        return render_template('task_1.html')
    else:
        code = request.form.get('code')
        if check_task_1(code):
            return render_template('success.html')
        else:
            return render_template('failure.html')


@app.route('/task_2', methods=['GET', 'POST'])
def task_2():
    if request.method == 'GET':
        return render_template('task_2.html')
    else:
        code = request.form.get('code')
        if check_task_2(code):
            return render_template('success.html')
        else:
            return render_template('failure.html')


@app.route('/task_3', methods=['GET', 'POST'])
def task_3():
    if request.method == 'GET':
        return render_template('task_3.html')
    else:
        code = request.form.get('code')
        if check_task_3(code):
            return render_template('success.html')
        else:
            return render_template('failure.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/failure')
def failure():
    return render_template('failure.html')


def check_task_1(code):
    global x

    x = 4
    exec(code, globals())
    if my_result != 'spring':
        return False

    x = 6
    exec(code, globals())
    if my_result != 'summer':
        return False

    x = 1
    exec(code, globals())
    if my_result != 'winter':
        return False

    x = 9
    exec(code, globals())
    if my_result != 'autumn':
        return False

    return True


def check_task_2(code):
    global n

    n = 12
    exec(code, globals())
    if my_result != 3:
        return False

    n = 2
    exec(code, globals())
    if my_result != 2:
        return False

    n = 299
    exec(code, globals())
    if my_result != 20:
        return False

    n = 1000
    exec(code, globals())
    if my_result != 1:
        return False

    return True


def check_task_3(code):
    global avg_salary
    global days

    avg_salary = 10000
    days = 14
    exec(code, globals())
    if my_result != 4778:
        return False

    avg_salary = 23000
    days = 10
    exec(code, globals())
    if my_result != 7849:
        return False

    avg_salary = 1
    days = 5
    exec(code, globals())
    if my_result != 0:
        return False

    avg_salary = 123111
    days = 0
    exec(code, globals())
    if my_result != 0:
        return False

    return True


if __name__ == '__main__':
    global my_result
    app.run(debug=True)
