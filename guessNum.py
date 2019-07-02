# 產生一個隨機integer（1～100）
# 讓使用者重複輸入數字去猜
# 猜對的話，印出“終於猜對了”
# 猜錯的話，要告訴他比答案大還是小

import random

ans = random.randint(1, 100)
attemptTimes = 0

while True:
	gusNum = input('請輸入要猜測的數字，介於1～100內： ')
	gusNum = int(gusNum)
	attemptTimes = attemptTimes + 1
	if gusNum == ans:
		print('終於猜對了！你總共嘗試了', attemptTimes,'次')
		break
	else:
		print('猜錯了')
		if gusNum > ans:
			print('你猜的數字比較大')
		elif gusNum < ans:
			print('你猜的數字比較小')