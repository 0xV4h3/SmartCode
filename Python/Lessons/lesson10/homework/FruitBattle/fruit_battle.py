import random, msvcrt, os, time

SIZE = 15
FRUITS = ['🍌','🍎','🍇','🍒','🍉']
TICK_DELAY = 0.1

def clear():
    os.system('cls')

def choose_character():
    clear()
    chars = ['🐒','🐶','🦊','🐼']
    print("Choose your character:")
    for i, c in enumerate(chars, 1):
        print(f" {i}. {c}")
    while True:
        k = msvcrt.getwch()
        if k.isdigit() and 1 <= int(k) <= len(chars):
            return chars[int(k)-1]

def choose_duration():
    clear()
    opts = [30, 60, 120]
    print("Choose game duration:")
    for i, d in enumerate(opts, 1):
        print(f" {i}. {d} seconds")
    while True:
        k = msvcrt.getwch()
        if k.isdigit() and 1 <= int(k) <= len(opts):
            return opts[int(k)-1]

def draw(monkey, snake, fruit, fruit_icon, ms, ss, left, player_char):
    clear()
    print(f"⏱ Time left: {left:3d}s   You: {ms}   Snake: {ss}")
    print('#' * (SIZE*2 + 3))
    for i in range(SIZE):
        row = ['# ']
        for j in range(SIZE):
            if (i,j) == monkey:
                cell = f"{player_char}"
            elif (i,j) == snake:
                cell = '🐍'
            elif (i,j) == fruit:
                cell = f"{fruit_icon}"
            else:
                cell = '. '
            row.append(cell)
        row.append('#')
        print(''.join(row))
    print('#' * (SIZE*2 + 3))
    print("\nUse arrows or WASD, 'q' to quit.")

def main():
    player_char = choose_character()
    duration    = choose_duration()

    monkey = (SIZE//2, SIZE//2)
    snake  = (random.randrange(SIZE), random.randrange(SIZE))
    while snake == monkey:
        snake = (random.randrange(SIZE), random.randrange(SIZE))
    fruit = (random.randrange(SIZE), random.randrange(SIZE))
    fruit_icon = random.choice(FRUITS)

    ms = ss = 0
    start = time.time()
    tick = 0

    while True:
        elapsed = int(time.time() - start)
        if elapsed >= duration:
            break
        left = duration - elapsed

        direction = None
        if msvcrt.kbhit():
            k = msvcrt.getwch()
            if k == '\xe0':
                k2 = msvcrt.getwch()
                dmap = {'H':(-1,0),'P':(1,0),'K':(0,-1),'M':(0,1)}
                direction = dmap.get(k2)
            else:
                ku = k.upper()
                wmap = {'W':(-1,0),'S':(1,0),'A':(0,-1),'D':(0,1)}
                if ku in wmap:
                    direction = wmap[ku]
                elif ku == 'Q':
                    return

        if direction:
            ni = monkey[0] + direction[0]
            nj = monkey[1] + direction[1]
            if 0 <= ni < SIZE and 0 <= nj < SIZE:
                monkey = (ni, nj)

        if tick % 2 == 0:
            dx, dy = fruit[0] - snake[0], fruit[1] - snake[1]
            if abs(dx) > abs(dy):
                step = (1 if dx>0 else -1, 0)
            else:
                step = (0, 1 if dy>0 else -1)
            si = snake[0] + step[0]
            sj = snake[1] + step[1]
            if 0 <= si < SIZE and 0 <= sj < SIZE:
                snake = (si, sj)

        if monkey == fruit:
            ms += 1
            while True:
                f = (random.randrange(SIZE), random.randrange(SIZE))
                if f != monkey and f != snake:
                    fruit = f
                    fruit_icon = random.choice(FRUITS)
                    break
        elif snake == fruit:
            ss += 1
            while True:
                f = (random.randrange(SIZE), random.randrange(SIZE))
                if f != monkey and f != snake:
                    fruit = f
                    fruit_icon = random.choice(FRUITS)
                    break

        draw(monkey, snake, fruit, fruit_icon, ms, ss, left, player_char)

        tick += 1
        time.sleep(TICK_DELAY)

    clear()
    print("\n=== Game Over ===")
    if ms > ss:
        print("🎉 You win!")
    elif ms < ss:
        print("🐍 Snake wins!")
    else:
        print("🤝 It's a tie!")

if __name__ == '__main__':
    main()