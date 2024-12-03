import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)
def get_list ():
    return """
    <html>
        <head>
            <title>Bienvenidos</title>
        </head>
        <body>
            <h1>Soy un título</h1>
            <p> Esto es un párrafo </p>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()