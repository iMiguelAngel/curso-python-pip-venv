import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')    #ruta principal
def get_list():
    return [1,2,3]

@app.get('/contact', response_class = HTMLResponse)
def get_html():
    return '''
            <html>
                <head>
                    <title>Some HTML in here</title>
                </head>
                <body>
                    <h1>Look ma! HTML!</h1>
                    <p>I'm a paragraph</p>
                </body>
            </html>
'''


def run():
    # requests
    store.get_categories()


if __name__ == '__main__':
    run()