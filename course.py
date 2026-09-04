python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민']
name = '이서연'

report = {'python':4, 'both':2, 'total':5}

both = set(python_list)&set(web_list)
all_students = set(python_list)|set(web_list)
only_py = set(python_list)-set(web_list)
only_web = set(web_list)-set(python_list)
one_only = set(python_list)^set(web_list)

print(f'파이썬 신청', len(python_list), f'건 -> 실제', len(set(python_list)), f'명')
print(f'웹개발 신청', len(web_list), f'건 -> 실제', len(set(web_list)), f'명')
print(sorted(set(python_list)))
print(sorted(set(web_list)))

print(f'둘 다 수강:', both)
print(f'전체 수강생:', all_students)
print(f'파이썬만:', only_py)
print(f'웹개발만:', only_web)
print(f'한 과목만:', one_only)

print(name, f'파이썬 수강?', bool(name in python_list))
print(name, f'웹개발 수강?', bool(name in web_list))
print(name, f'둘 다 수강?', bool(name in both))
print(name, f'하나라도 수강?', bool(name in python_list or web_list))
print(name, f'미수강?', bool(name not in all_students))
print(name, f'교집합이 비었나?', not bool(both))

print(report)
print("="*32)
print(f'{"수 강 현 황":^18}')
print('='*32)
print(f'{"파이썬":<14}', f'{len(set(python_list)):>10}', f'명')
print(f'{"웹개발":<14}', f'{len(set(web_list)):>10}', f'명')
print("_"*32)
print(f'{"둘 다 수강":<14}', f'{len(both):>10}', f'명')
print(f'{"전체 인원":<14}', f'{len(all_students):>10}', f'명')
print("="*32)
print(f'{"전체 수강률:":<14}', f'{len(both)/len(all_students)*100:.1f}',f"%")