jumin = "990101-1234567"
card = "1234-5678-9012-3456"


jumin_secret = jumin.replace('234567', '******')
card_secret = card.replace(card[:15], '*'*14)


print(jumin_secret)
print(len(jumin_secret))
print(card_secret)