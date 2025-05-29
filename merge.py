import pickle
train_head = pickle.load(open('data/nuscenes/nuscenes_wo_vir_feat_dbinfos_train.pkl', 'rb'))
val_head = pickle.load(open('data/nuscenes/nuscenes_val_wo_vir_feat_head_50split_dbinfos_train.pkl', 'rb'))
train_tail = pickle.load(open('data/nuscenes/nuscenes_wo_vir_feat_tail_50split_dbinfos_train.pkl', 'rb'))
val_tail = pickle.load(open('data/nuscenes/nuscenes_val_wo_vir_feat_tail_50split_dbinfos_train.pkl', 'rb'))
trainval = dict()
#trainval['infos'] = train_head['infos'] + val_head['infos'] + train_tail['infos'] +val_tail['infos']
#trainval['metadata'] = train_head['metadata']
for key in train_head:
    val_h = val_head[key] if val_head.get(key) else []
    val_t = val_tail[key] if val_tail.get(key) else []
    train_h = train_head[key] if train_head.get(key) else []
    train_t = train_tail[key] if train_tail.get(key) else []
    trainval[key] = train_h + train_t
    
import mmcv
mmcv.dump(trainval, 'nuscenes_dbinfos_train100.pkl')

