import random

print('数当てゲームを始めます！')

answer = random.randint(1, 100)
count = 0

while True:
    guess = input("1～100の数字を入力してください: ")
    guess = int(guess)
    count += 1

    if guess == answer:
        print("正解！")
        print(f"あなたは{count}回で正解しました！")
        break
    elif guess < answer:
        print("もっと大きい数字です")
    else:
        print("もっと小さい数字です")
