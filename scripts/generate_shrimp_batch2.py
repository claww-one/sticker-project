import os

def generate_shrimp_boss_batch2(name, theme, folder="stickers/batch2"):
    os.makedirs(folder, exist_ok=True)
    width, height = 512, 512
    grid_w, grid_h = 100, 100
    header = f"P3\n{width} {height}\n255\n"
    bg = "255 255 255"
    red = "230 50 30"
    light_red = "255 100 80"
    dark_red = "150 20 10"
    black = "30 15 10"
    white = "255 255 255"
    gold = "255 215 0"
    neon_blue = "50 150 255"
    coffee_brown = "111 78 55"
    fire_orange = "255 69 0"
    
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]

    def p(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h: data[y][x] = color
    def fill_rect(x1, y1, x2, y2, color):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1): p(x, y, color)

    # --- CORE SHRIMP BOSS DRAWING ---
    def draw_shrimp(bx, by, scale=1.0, mood="neutral", r_claw_pos="down", l_claw_pos="down"):
        bw, bh = int(28*scale), int(35*scale)
        fill_rect(bx - bw//2, by - bh//2, bx + bw//2 - 1, by + bh//2 - 1, red)
        # Segments
        for sy in [by - bh//4, by, by + bh//4]: fill_rect(bx - bw//2, sy, bx + bw//2 - 1, sy, dark_red)
        # Outline
        for y in range(by - bh//2, by + bh//2): p(bx - bw//2 - 1, y, black); p(bx + bw//2, y, black)
        fill_rect(bx - bw//2, by - bh//2 - 1, bx + bw//2 - 1, by - bh//2 - 1, black)
        fill_rect(bx - bw//2, by + bh//2, bx + bw//2 - 1, by + bh//2, black)
        
        # Eyes
        eye_y = by - int(10*scale)
        fill_rect(bx - int(8*scale), eye_y, bx - int(5*scale), eye_y+3, white)
        fill_rect(bx + int(4*scale), eye_y, bx + int(7*scale), eye_y+3, white)
        p(bx - int(7*scale), eye_y+1, black); p(bx + int(5*scale), eye_y+1, black)
        
        # Antennae (Mood-based)
        if mood == "angry":
            for i in range(12):
                p(bx - int(5*scale) - i, eye_y - 2 - i, black) # V shape
                p(bx + int(5*scale) + i, eye_y - 2 - i, black)
        elif mood == "shock":
            for i in range(15):
                p(bx - int(6*scale), eye_y - 2 - i, black) # Vertical
                p(bx + int(6*scale), eye_y - 2 - i, black)
        else:
            for i in range(int(15*scale)):
                p(bx - int(5*scale) - i, eye_y - 2 - i//2, black)
                p(bx + int(5*scale) + i, eye_y - 2 - i//2, black)

        # Claws
        def draw_claw(cx, cy, special=None):
            r = int(15*scale)
            for y in range(cy-r, cy+r+1):
                for x in range(cx-r, cx+r+1):
                    if (x-cx)**2 + (y-cy)**2 <= r**2: p(x, y, red)
                    if (r-1.5)**2 <= (x-cx)**2 + (y-cy)**2 <= r**2: p(x, y, black)
            p(cx + int(3*scale), cy - int(5*scale), light_red)

        l_cx, l_cy = bx - int(25*scale), by
        r_cx, r_cy = bx + int(25*scale), by
        
        if l_claw_pos == "up": l_cy -= int(20*scale)
        if r_claw_pos == "up": r_cy -= int(20*scale)
        if l_claw_pos == "cross": l_cx, l_cy = bx - int(10*scale), by
        if r_claw_pos == "cross": r_cx, r_cy = bx + int(10*scale), by

        draw_claw(l_cx, l_cy)
        draw_claw(r_cx, r_cy)

    # --- THEMES BATCH 2 ---
    if theme == "working":
        draw_shrimp(50, 50, 0.9)
        fill_rect(20, 70, 80, 85, "100 100 100") # Keyboard
        for i in range(5): p(30+i*10, 75, neon_blue)
    elif theme == "angry":
        draw_shrimp(50, 55, 1.1, mood="angry", r_claw_pos="up", l_claw_pos="up")
        fill_rect(20, 80, 80, 90, "139 69 19") # Table slam
    elif theme == "rich":
        draw_shrimp(50, 60, 1.0)
        # Falling dollars
        for _ in range(10):
            import random
            rx, ry = random.randint(10, 90), random.randint(10, 40)
            fill_rect(rx, ry, rx+5, ry+3, "50 200 50")
    elif theme == "sleepy":
        draw_shrimp(50, 60, 1.0, mood="neutral")
        p(60, 45, neon_blue); p(65, 40, neon_blue) # Zzz
    elif theme == "coffee":
        draw_shrimp(50, 55, 1.0, r_claw_pos="up")
        fill_rect(70, 40, 85, 55, white) # Cup
        fill_rect(72, 42, 83, 45, coffee_brown)
    elif theme == "heart":
        draw_shrimp(50, 55, 1.0, r_claw_pos="cross", l_claw_pos="cross")
        # Heart shape
        for i in range(5):
            p(50+i, 30+i, "255 50 150"); p(50-i, 30+i, "255 50 150")
            p(45+i, 25, "255 50 150"); p(55-i, 25, "255 50 150")
    elif theme == "shock":
        draw_shrimp(50, 60, 1.2, mood="shock")
    elif theme == "fire":
        # Background fire
        for _ in range(30):
            import random
            fill_rect(random.randint(10, 90), random.randint(60, 95), random.randint(10, 90), 99, fire_orange)
        draw_shrimp(50, 55, 1.0, mood="angry")
    elif theme == "no":
        draw_shrimp(50, 55, 1.0, r_claw_pos="cross", l_claw_pos="cross")
        # X mark
        for i in range(15): p(40+i, 40+i, "255 0 0"); p(55-i, 40+i, "255 0 0")
    elif theme == "lofi":
        draw_shrimp(50, 50, 0.9)
        # Headphones
        fill_rect(35, 40, 65, 42, black)
        fill_rect(32, 45, 38, 55, black); fill_rect(62, 45, 68, 55, black)

    # Save
    ppm_path = f"stickers/batch2/{name}.ppm"
    png_path = f"stickers/batch2/{name}.png"
    with open(ppm_path, 'w') as f:
        f.write(header)
        for y in range(height):
            gy = (y * grid_h) // height
            row = []
            for x in range(width):
                gx = (x * grid_w) // width
                row.append(data[gy][gx])
            f.write(" ".join(row) + "\n")
    os.system(f"convert {ppm_path} {png_path}")
    os.remove(ppm_path)

if __name__ == "__main__":
    themes = [
        ("01_working", "working"), ("02_angry", "angry"), ("03_rich", "rich"),
        ("04_sleepy", "sleepy"), ("05_coffee", "coffee"), ("06_heart", "heart"),
        ("07_shock", "shock"), ("08_fire", "fire"), ("09_no", "no"), ("10_lofi", "lofi")
    ]
    for name, t in themes:
        generate_shrimp_boss_batch2(name, t)
        print(f"Generated {name}")
