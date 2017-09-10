from contextlib import contextmanager


# class File(object):
#     """Context manager as Class"""
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         self.file_obj.close()
#
#
# with File('demo.txt', 'w') as opened_file:
#     opened_file.write('asdsda')


@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
