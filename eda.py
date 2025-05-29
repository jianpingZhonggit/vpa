import json
sub = json.load(open('submission/pts_bbox/results_nusc.json'))
print(type(sub))
print(sub.keys())
print(sub['meta'])
print(type(sub['results']))
print(len(sub['results']))
for res in sub['results']:
    print(res)
    print(sub['results'][res][0])
    print(len(sub['results'][res][0]))
    exit(0)