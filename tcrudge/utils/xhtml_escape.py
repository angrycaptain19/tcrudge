from functools import singledispatch

from tornado.escape import xhtml_escape


@singledispatch
def xhtml_escape_complex_object(obj):
    raise TypeError('Escaped object type must be a tuple, list, dict or str, not {}.'.format(type(obj)))


@xhtml_escape_complex_object.register(str)
def __xhtml_escape_str(obj):
    return xhtml_escape(obj)


@xhtml_escape_complex_object.register(dict)
def __xhtml_escape_object_dict(obj):
    return {k: xhtml_escape_complex_object(v) for k, v in obj.items()}


@xhtml_escape_complex_object.register(list)
@xhtml_escape_complex_object.register(tuple)
def __xhtml_escape_list(obj):
    return tuple(xhtml_escape_complex_object(i) for i in obj)
