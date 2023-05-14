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
    if execute_code_task1(code, 4) != 'spring':
        return False

    if execute_code_task1(code, 6) != 'summer':
        return False

    if execute_code_task1(code, 1) != 'winter':
        return False

    if execute_code_task1(code, 9) != 'autumn':
        return False

    return True


def execute_code_task1(code, a):
    global x
    x = a
    exec(code, globals())
    return my_result


def check_task_2(code):

    if execute_code_task2(code, 12) != 3:
        return False

    if execute_code_task2(code, 2) != 2:
        return False

    if execute_code_task2(code, 299) != 20:
        return False

    if execute_code_task2(code, 1000) != 1:
        return False

    return True


def execute_code_task2(code, a):
    global n
    n = a
    exec(code, globals())
    return my_result


def check_task_3(code):
    if execute_code_task3(code, 10000, 14) != 4778:
        return False

    if execute_code_task3(code, 23000, 10) != 7849:
        return False

    if execute_code_task3(code, 1, 5) != 0:
        return False

    if execute_code_task3(code, 123111, 0) != 0:
        return False

    return True


def execute_code_task3(code, a, b):
    global avg_salary
    global days
    avg_salary = a
    days = b
    exec(code, globals())
    return my_result


if __name__ == '__main__':
    global my_result
    app.run(debug=True)
