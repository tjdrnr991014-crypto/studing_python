product_name = input("상품명")
number = int(input("수량"))
price = int(input("단가"))



print("="*38)
print(f'{"영 수 증":^8}')
print("="*38)
print(f'{product_name:<10}', f'{number:^8}', f'{price*number:>6,}')
print("ㅡ"*20)
print(f'{"부가세(10%)":<10}', f'{price*number*0.1:>6,}')
print(f'{"합계":<10}', f'{price*number+price*number*0.1:>6,}')
print("="*38)