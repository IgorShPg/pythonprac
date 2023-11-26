import sys

text=sys.stdin.buffer.read()
text=text.decode('UTF-8').encode("latin-1",errors='replace').decode('cp1251',errors='replace')
sys.stdout.buffer.write(text.encode('UTF-8'))
