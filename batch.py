import os
for fol in os.listdir('work_dirs'):
    for j in range(9):
        print(f'work_dirs/{fol}/epoch_{j}.pth')
        os.system(f'rm -rf work_dirs/{fol}/epoch_{j}.pth')
