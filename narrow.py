idata = {
    'data':[
        {'d':{'e':'f', 'l':'m', 's': 'w'}},
        {'q':{'e':'g', 'l':'m', 's': 'w'}},
        {'w':{'e':'h', 'l':'m', 's2': 'w'}},
        {'z':{'e':'i', 'l':'m', 's2': 'w'}},
        'xxx'
    ], 
    'b':'c', 
    'w':{
        'x':{
            'z':'y'
            }
        }
    }
zidata = {
    'data':{
        'd':[{'e':'f', 'l':'m', 's': 'w'}, {'e':'z', 'l':'e', 's': 'qqq'}],
        'q':{'e':'g', 'l':'m', 's': 'w'},
        'w':{'e':'h', 'l':'m', 's2': 'w'},
        'z':{'e':'i', 'l':'m', 's2': 'w'},
    }
} 
path = 'data.d.e'
paths = ['data.d.e', 'data.d.s', 'data.q.l', 'data.q.l.z', 'data.q.l', 'data.d.e.f.g', 'data.d.h','meta', 'data.z.k']

import pprint 

def paths_to_dict(paths):
    res = {}
    sp = sorted(paths)
    spaths = []
    for p in sp:
        if p not in spaths:
            spaths.append(p)
    for p in spaths:
        eles = p.split('.') 
        r = res
        for ele in eles:
            if ele not in r:
                r[ele] = {}
                r = r[ele]
            else:
                if r[ele] == {}:
                    break
                r = r[ele]
    return res



res = paths_to_dict(paths)
print(res)
print('-----------------------')

def prune(dic, data):
    if not dic:
        return
    #print(dic)
    ks = dic.keys()
    if not isinstance(data, dict):
        if isinstance(data, list):
            to_be_rm = []
            for idx in range(len(data)):
                if not isinstance(data[idx], dict) and not isinstance(data[idx], list):
                    to_be_rm.append(data[idx])
                else:
                    prune(dic, data[idx])
            try:
                for tbr in to_be_rm:
                    #print('remove', tbr)
                    data.remove(tbr)
                while True:
                    data.remove({})
                    #print('remove', '{}')
            except:
                pass
        else:
            return
    cd = data.copy()
    if isinstance(data, dict):
        for it in cd.items():
            #print('****it', it, 'xxx', it[0], 'xxx', k)
            if it[0] not in ks:
                del data[it[0]]
                print('ks', ks)
                print('remove+', it[0])
            else:
                prune(dic[it[0]], data[it[0]])
    return data
dic = paths_to_dict(paths)
res = prune(dic, idata)
print('+++++++++++++++++++')
pprint.pprint(res)
print('+++++++++++++++++++')
ikeys = path.split('.')
def test(keys, data):
    #paths_to_dict(paths)
    if len(keys) == 0:
        return
    print(keys)
    k = keys.pop(0)
    if not isinstance(data, dict):
        if isinstance(data, list):
            to_be_rm = []
            for idx in range(len(data)):
                if not isinstance(data[idx], dict) and not isinstance(data[idx], list):
                    to_be_rm.append(data[idx])
                else:
                    test([k] + keys, data[idx])
            try:
                for tbr in to_be_rm:
                    data.remove(tbr)
                while True:
                    data.remove({})
            except:
                pass
        else:
            return
    
    cd = data.copy()
    if isinstance(data, dict):
        for it in cd.items():
            #print('****it', it, 'xxx', it[0], 'xxx', k)
            if it[0] != k:
                del data[it[0]]
            else:
                test(keys, data[it[0]])
    return data


#ret = test(ikeys, idata)
#print(ret)
