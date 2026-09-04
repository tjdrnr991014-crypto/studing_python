seconds = 3725
hour = seconds // 3600
minute = seconds % 3600 // 60
seconds_now = seconds % 3600 - 120


print(f"{hour}시간 {minute}분 {seconds_now}초")