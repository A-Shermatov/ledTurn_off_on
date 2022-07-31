from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def index(request: Request):
    return HTMLResponse(content="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Led turn on\off</title>
</head>
<body>
    <form action="/form" method="get">
        <input type="radio" id="on" name="led" value="1">
        <label for="on"> Turn on</label><br>
        <input type="radio" id="off" name="led" value="0">
        <label for="off"> Turn off</label><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
        """, status_code=200)


@app.get('/form')
def index(request: Request, led: int):
    if led:
        return HTMLResponse(content="""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Led turn on\off</title>
        </head>
        <body>
            <h1> Turned off</h1>
            <form action="/form" method="get">
                <input type="radio" id="on" name="led" value="1">
                <label for="on"> Turn on</label><br>
                <input type="radio" id="off" name="led" value="0">
                <label for="off"> Turn off</label><br>
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
                """, status_code=200)
    return HTMLResponse(content="""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Led turn on\off</title>
            </head>
            <body>
                <h1> Turned off</h1>
                <form action="/form" method="get">
                    <input type="radio" id="on" name="led" value="1">
                    <label for="on"> Turn on</label><br>
                    <input type="radio" id="off" name="led" value="0">
                    <label for="off"> Turn off</label><br>
                    <button type="submit">Submit</button>
                </form>
            </body>
            </html>
                    """, status_code=200)



