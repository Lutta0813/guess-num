# 產生一個隨機integer（1～100）
# 讓使用者重複輸入數字去猜
# 猜對的話，印出“終於猜對了”
# 猜錯的話，要告訴他比答案大還是小

import random

firstNum = input('請輸入最小數字： ')
lastNum = input('請輸入最大數字： ')
firstNum = int(firstNum)
lastNum = int(lastNum)

while True:
	if firstNum > lastNum:
		print('最小數字大於最大數字，請重新輸入')
		break
	elif firstNum < lastNum:
		ans = random.randint(firstNum, lastNum)
		attemptTimes = 0
		while True:
			# gusNum = input('請輸入要猜測的數字，數字介於', firstNum, '到', lastNum, '之間')
			print('提示：數字介於', firstNum, '跟', lastNum, '之間')
			gusNum = input('請輸入要猜測的數字')
			gusNum = int(gusNum)
			attemptTimes = attemptTimes + 1
			if gusNum == ans:
				print('終於猜對了！你總共嘗試了', attemptTimes,'次，遊戲結束！')
				break
			else:
				print('猜錯了')
				if gusNum > ans:
					print('你猜的數字比較大')
				elif gusNum < ans:
					print('你猜的數字比較小')
		break
	else:
		print('最小數字等於最大數字，請重新輸入')
		break

