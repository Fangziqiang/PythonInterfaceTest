# If stderr is not easily accessible for you, you can redirect the output to a file:
@pysnooper.snoop('/my/log/file.log')

# You can also pass a stream or a callable instead, and they'll be used.
# See values of some expressions that aren't local variables:
@pysnooper.snoop(watch=('foo.bar', 'self.x["whatever"]'))

# Expand values to see all their attributes or items of lists/dictionaries:
@pysnooper.snoop(watch_explode=('foo', 'self'))
# This will output lines like:
'''
Modified var:.. foo[2] = 'whatever'
New var:....... self.baz = 8
'''
# (see Advanced Usage for more control):
import pysnooper
@pysnooper.snoop(watch=(
    pysnooper.Attrs('x'),    # attributes
    pysnooper.Keys('y'),     # mapping (e.g. dict) items
    pysnooper.Indices('z'),  # sequence (e.g. list/tuple) items
))

# Show snoop lines for functions that your function calls:
@pysnooper.snoop(depth=2)

Start all snoop lines with a prefix, to grep for them easily:

@pysnooper.snoop(prefix='ZZZ ')
On multi-threaded apps identify which thread are snooped in output:

@pysnooper.snoop(thread_info=True)
PySnooper supports decorating generators.

You can also customize the repr of an object:

def large(l):
    return isinstance(l, list) and len(l) > 5

def print_list_size(l):
    return 'list(size={})'.format(len(l))

def print_ndarray(a):
    return 'ndarray(shape={}, dtype={})'.format(a.shape, a.dtype)

@pysnooper.snoop(custom_repr=((large, print_list_size), (numpy.ndarray, print_ndarray)))
def sum_to_x(x):
    l = list(range(x))
    a = numpy.zeros((10,10))
    return sum(l)

sum_to_x(10000)
You will get l = list(size=10000) for the list, and a = ndarray(shape=(10, 10), dtype=float64) for the ndarray. The 
custom_repr are matched in order, if one condition matches, no further conditions will be checked.