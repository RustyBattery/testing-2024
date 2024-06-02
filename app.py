from flask import Flask, request, abort
from solution import Solution
from werkzeug import exceptions

app = Flask(__name__)
solution = Solution()


@app.get('/')
def form():
    html = '<html lang><body><h1>Max product</h1>' \
           '<form action="/" method="POST">' \
           '<input type="text" name="data">' \
           '<input type="submit">' \
           '</form>' \
           '</body></html>'
    return html


@app.post('/')
def max_product():
    try:
        data = request.form['data']
        nums = list(map(int, data.split()))
        return {"res": solution.maxProduct(nums)}
    except AssertionError:
        abort(400)
    except TypeError:
        abort(400)
    except ValueError:
        abort(400)
    except exceptions.BadRequestKeyError:
        abort(400)
