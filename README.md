Hurricane
==========

Hurricane is an attempt to make Tornado more friendly for API developers. You can still use all the functionality that Tornado provides, Hurricane will just act as a wrapper
to make Tornado more friendly.

With tornado you would have to define a class and its methods but Hurricane provides Flask-like functionality to do the same with a function and a decorator.
In that decorator you specify the route and the method allowed for the request.

Then all you have to do is run the app at the specified port.

```python
from hurricane import Hurricane

api = Hurricane()

@api.route(r"/say/hello", 'GET')
def say_hello(handler):
    handler.write('Hello!')

api.run(8888)
```
