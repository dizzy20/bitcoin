import pyupbit

access = "HxeoCbN9dkBL3RGYDdAkNKMRsfDOVd7mXKEoatJr"          # 본인 값으로 변경
secret = "zmUIxPSFQxXGIUxUKxBA7QYzOQ1YOxxVXV1Wu2om"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
