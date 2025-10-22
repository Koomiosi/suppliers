from waitress import serve
from suppliers.wsgi import application

if __name__ == '__main__':
    print("Open browser in https://localhost:8000")
    serve(application, port='8000')