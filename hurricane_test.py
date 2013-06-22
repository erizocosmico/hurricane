from hurricane import *

app = Hurricane()

@app.route(r"/say/hello")
def sayhello(handler):
    handler.write('Hello!')
    
@app.route(r"/say/goodbye")
def saygoodbye(handler):
    handler.write('Goodbye!')

if __name__ == '__main__': 
    app.run(8888)