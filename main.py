from flask import Flask

app = Flask(__name__)


@app.route('/')
def i():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми '
                                                                                               'безжизненные пока '
                                                                                               'планеты.',
                      'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="https://w7.pngwing.com/pngs/16/806/png-transparent-planet-mars-illustration-earth-terrestrial-planet-mars-solar-system-mars-sphere-venus-astronomical-object-thumbnail.png" alt="альтернативный текст">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link href="static/css/style.css" rel="stylesheet" />
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                            
                          </head>
                          <body>
                            <h1 style="color:red">Жди нас, Марс!</h1>
                            <img src="static/img/mars.png" alt="альтернативный текст">
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-secondary">Человечество вырастает из детства</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-success">Человечеству мала одна планета</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-secondary">Мы сделаем обитаемыми безжизненные пока планеты</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-warning">И начнем с Марса!</a>
                            <a style="height:50px; font-size: 25px" href="#" class="list-group-item list-group-item-action list-group-item-danger">Присоединяйся!</a>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
