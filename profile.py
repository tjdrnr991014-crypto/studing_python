student = {'name':'김민준', 'age':20, 'major':'컴퓨터공학'}
student['email'] = 'minjun@example.com'
student['hobbies'] = ['python', 'game']
student['age'] = 21
del student['major']

student.keys()
student.values()
student.items()


print(student)
print(list(student.values()))
print(len(student))
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone','등록되지 않음'))
print('email' in student, 'major' in student)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

print("="*34)
print(f'{"PROFILE":^8}')
print("="*34)
print(f'{"이름":<12}', f'{student.get("name"):>18}')
print(f'{"나이":<12}', f'{student.get("age"):>18}')
print(f'{"이메일":<12}', f'{student.get("email"):>18}')
print(f'{"전화":<12}', f'{student.get("전화", "미등록"):>18}')
print("-"*34)
print(f'{"취미":<12}', f'{str(student.get("hobbies")):>18}')
print(f'{"항목 수":<12}', f'{len(student):>18}')
print("="*34)