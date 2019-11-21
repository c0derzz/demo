import random
rule = {1: "拳头", 2: "布", 3: "剪刀"}
rule_desc = "请您输入您要出示的拳 " + str(rule)
# 提示玩家出拳
player = int(input(rule_desc))
if player not in[1, 2, 3]:
    print("请出示 1 或 2 或 3")
else:

    # 电脑出拳
    computer = random.randint(1, 3)
    print("玩家出拳为%s - 电脑出拳为 %s" % (rule[player], rule[computer]))
    # 比较出拳结果

    if ((player == 1 and computer == 3)
            or (player == 2 and computer == 1)
            or (player == 3 and computer == 2)):

        print("选手胜利")
    elif player == computer:
        print("平局")
    else:
        print("电脑获胜")
