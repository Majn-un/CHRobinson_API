from flask import Flask, jsonify
from anytree import Node, search

usa = Node("USA")
can = Node("CAN", parent=usa)
mex = Node("MEX", parent=usa)
blz = Node("BLZ", parent=mex)
gtm = Node("GTM", parent=mex)
slv = Node("SLV", parent=gtm)
hnd = Node("HND", parent=gtm)
nic = Node("NIC", parent=hnd)
cri = Node("CRI", parent=nic)
pan = Node("PAN", parent=cri)

app = Flask(__name__)


@app.route('/<string:arg>')
def hello_world(arg: str):
    res = search.find(usa, lambda node: node.name == arg.upper())
    if res is None:
        return "Not a proper response"

    res = str(res)
    res = res[7:-2].split("/")

    return jsonify(
        destination=arg,
        list=res
    ), 200


if __name__ == '__main__':
    app.run()
