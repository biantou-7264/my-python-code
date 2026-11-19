import os

path = '/Users/luojingfeng/Documents/'
pythons = 0
files = {}

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() == '.py':
        pythons += 1
        file_io = open(os.path.join(path, file), 'r')
        line_count = len(file_io.readlines())
        file_io.seek(0)
        imports = file_io.read().count('import')
        files[name] = {'line_count': line_count, 'imports': imports}
        file_io.close()


for key, value in files.items():
    print('file: %s' % key)
    print('lines: %s' % value['line_count'])
    print('imports: %s' % value['imports'])
    print('=' * 20)
print('count: %s' % pythons)
