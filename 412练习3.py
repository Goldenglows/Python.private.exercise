mc = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

MC = {k.lower():mc.get(k.lower(),0)+mc.get(k.upper(),0) for k in mc.keys() if k.lower() in ['a','b','z']}

print(MC)