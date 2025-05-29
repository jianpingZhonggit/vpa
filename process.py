import os
for _ in os.listdir('work_dirs'):
    # for i in os.listdir(f'work_dirs/{_}'):
    for k in range(10):
        os.system(f'rm -rf work_dirs/{_}/epoch_{k}.pth')