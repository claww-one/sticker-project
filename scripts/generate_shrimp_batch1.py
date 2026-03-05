import os

def generate_shrimp_boss_batch(name, theme, folder="stickers/batch1"):
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
    dark_gold = "180 140 0"
    neon_green = "50 255 50"
    neon_blue = "50 150 255"
    ice_blue = "180 230 255"
    wood_brown = "139 69 19"
    
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]

    def p(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h: data[y][x] = color
    def fill_rect(x1, y1, x2, y2, color):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1): p(x, y, color)

    # --- CORE LOBSTER DRAWING ---
    def draw_lobster(bx, by, scale=1.0, mood="neutral", r_claw_pos="down", l_claw_pos="down"):
        bw, bh = int(28*scale), int(35*scale)
        fill_rect(bx - bw//2, by - bh//2, bx + bw//2 - 1, by + bh//2 - 1, red)
        for sy in [by - bh//4, by, by + bh//4]: fill_rect(bx - bw//2, sy, bx + bw//2 - 1, sy, dark_red)
        for y in range(by - bh//2, by + bh//2): p(bx - bw//2 - 1, y, black); p(bx + bw//2, y, black)
        fill_rect(bx - bw//2, by - bh//2 - 1, bx + bw//2 - 1, by - bh//2 - 1, black)
        fill_rect(bx - bw//2, by + bh//2, bx + bw//2 - 1, by + bh//2, black)
        
        # Eyes
        eye_y = by - int(10*scale)
        fill_rect(bx - int(8*scale), eye_y, bx - int(5*scale), eye_y+3, white)
        fill_rect(bx + int(4*scale), eye_y, bx + int(7*scale), eye_y+3, white)
        p(bx - int(7*scale), eye_y+1, black); p(bx + int(5*scale), eye_y+1, black)
        
        # Antennae
        for i in range(int(15*scale)):
            p(bx - int(5*scale) - i, eye_y - 2 - i//2, black)
            p(bx + int(5*scale) + i, eye_y - 2 - i//2, black)

        # Claws
        def draw_claw(cx, cy):
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
        if l_claw_pos == "mouth": l_cx, l_cy = bx - int(10*scale), by - int(5*scale)
        
        draw_claw(l_cx, l_cy)
        draw_claw(r_cx, r_cy)

    # --- THEMES ---
    if theme == "throne":
        # Throne
        fill_rect(20, 40, 80, 80, gold); fill_rect(25, 45, 75, 75, dark_gold)
        draw_lobster(50, 55, 0.8)
    elif theme == "eye":
        draw_lobster(50, 55, 1.2)
        # Big red eye
        fill_rect(42, 42, 58, 50, black)
        fill_rect(45, 44, 55, 48, "255 0 0") # Glow
    elif theme == "approve":
        draw_lobster(50, 55, 1.0, r_claw_pos="up")
        # Green pass symbol
        for i in range(10): p(70+i, 35-i, neon_green); p(70-i, 35-i, neon_green)
    elif theme == "dismiss":
        draw_lobster(50, 55, 1.0, r_claw_pos="up")
        # Wave energy
        for i in range(3): fill_rect(80+i*5, 30, 81+i*5, 50, neon_blue)
    elif theme == "mute":
        draw_lobster(50, 55, 1.0, l_claw_pos="mouth")
        fill_rect(40, 50, 60, 52, black) # Mouth line
    elif theme == "visionary":
        draw_lobster(50, 55, 1.0)
        # Holographic map
        for _ in range(20):
            import random
            p(random.randint(20,80), random.randint(20,40), neon_blue)
    elif theme == "command":
        draw_lobster(50, 55, 1.0, r_claw_pos="up")
        fill_rect(20, 75, 80, 85, wood_brown) # Table
        # Impact
        fill_rect(70, 70, 85, 75, neon_blue)
    elif theme == "thinking":
        draw_lobster(50, 55, 1.0)
        # Gears
        fill_rect(45, 15, 55, 25, gold); p(50, 20, black)
    elif theme == "zero":
        draw_lobster(50, 55, 1.0)
        # Ice block
        for y in range(20, 90):
            for x in range(20, 80):
                if (x+y)%4 == 0: p(x, y, ice_blue)
    elif theme == "satisfied":
        draw_lobster(50, 55, 1.0, mood="happy")
        # Glow
        fill_rect(40, 30, 60, 35, "255 255 200")

    # Save
    ppm_path = f"stickers/batch1/{name}.ppm"
    png_path = f"stickers/batch1/{name}.png"
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
        ("01_throne", "throne"), ("02_eye", "eye"), ("03_approve", "approve"),
        ("04_dismiss", "dismiss"), ("05_mute", "mute"), ("06_visionary", "visionary"),
        ("07_command", "command"), ("08_thinking", "thinking"), ("09_zero", "zero"),
        ("10_satisfied", "satisfied")
    ]
    for name, t in themes:
        generate_shrimp_boss_batch(name, t)
        print(f"Generated {name}")
