# -*- coding: utf-8 -*-
import jsonpickle
import getopt
import sys
import random
import string
import os.path
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file name"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen, cont=False):
    symbols = string.ascii_letters + string.digits + "_"# + " "
    if cont: symbols = symbols + string.punctuation + " "*10 #contamination
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string("GroupName_", 10), header=random_string("GroupHeader_", 20), footer=random_string("GroupFooter_", 20))
    for i in range(n)
]# + [Group(name="", header="", footer="")]

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f), "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
