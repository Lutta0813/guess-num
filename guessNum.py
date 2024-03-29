# 產生一個隨機integer（1～100）
# 讓使用者重複輸入數字去猜
# 猜對的話，印出“終於猜對了”
# 猜錯的話，要告訴他比答案大還是小

import random

while True:

	smallestNum = input('請輸入最小數字： ')
	biggestNum = input('請輸入最大數字： ')
	smallestNum = int(smallestNum)
	biggestNum = int(biggestNum)

	if smallestNum > biggestNum:
		print('最小數字大於最大數字，請重新輸入')
	elif smallestNum < biggestNum:
		ans = random.randint(smallestNum, biggestNum)
		attemptTimes = 0
		while True:
			# gusNum = input('請輸入要猜測的數字，數字介於', smallestNum, '到', biggestNum, '之間')
			print('提示：數字介於', smallestNum, '跟', biggestNum, '之間')
			gusNum = input('請輸入要猜測的數字: ')
			gusNum = int(gusNum)
			attemptTimes = attemptTimes + 1
			if gusNum == ans:
				print('終於猜對了！你總共嘗試了', attemptTimes,'次，遊戲結束！')
				break
			else:
				print('猜錯了，這是你猜的第', attemptTimes, '次')
				if gusNum > ans:
					print('你猜的數字比較大')
				elif gusNum < ans:
					print('你猜的數字比較小')
		break
	else:
		print('最小數字等於最大數字，請重新輸入')

