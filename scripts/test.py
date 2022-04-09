import datetime
import sys

now = datetime.datetime.now()

output = f"""<p>This output is from the python script!</p><h2>Hello, {sys.argv[1]}</h2><ul><li><strong>Name: </strong> {sys.argv[1]}</li><li><strong>Email: </strong> {sys.argv[2]}</li><li><strong>Note: </strong> {sys.argv[3]}</li></ul>"""
print(output)
