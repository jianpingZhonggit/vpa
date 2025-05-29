import pickle
train = pickle.load(open('/data/jianpingzhong/xuezhzh/CMT-master/data/nuscenes/nuscenes_vpa_infos_train.pkl', 'rb'))
val = pickle.load(open('/data/jianpingzhong/xuezhzh/CMT-master/data/nuscenes/nuscenes_vpa_infos_val.pkl', 'rb'))
print(val.keys())
print(val['metadata'])
trainval = dict()
trainval['metadata'] = train['metadata']
trainval['infos'] = train['infos'] + val['infos']
with open('nuscenes_vpa_infos_trainval.pkl', 'wb') as f:
    pickle.dump(trainval, f)
