import os

def generate_shrimp_boss_batch3(name, theme, folder="batch3"):
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
    neon_green = "50 255 50"
    purple = "150 50 255"
    yellow = "255 255 0"
    
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
        if l_claw_pos == "cross": l_cx, l_cy = bx - int(10*scale), by
        if r_claw_pos == "cross": r_cx, r_cy = bx + int(10*scale), by
        
        draw_claw(l_cx, l_cy)
        draw_claw(r_cx, r_cy)

    # --- THEMES BATCH 3 ---
    if theme == "reading":
        draw_shrimp(50, 50, 0.9, l_claw_pos="cross", r_claw_pos="cross")
        fill_rect(35, 55, 65, 75, white) # Book
        fill_rect(35, 55, 37, 75, black); fill_rect(63, 55, 65, 75, black)
    elif theme == "gym":
        draw_shrimp(50, 60, 1.0, l_claw_pos="up", r_claw_pos="up")
        fill_rect(20, 30, 80, 35, "50 50 50") # Barbell
        fill_rect(15, 20, 25, 45, black); fill_rect(75, 20, 85, 45, black)
    elif theme == "celebration":
        draw_shrimp(50, 60, 1.0, r_claw_pos="up")
        # Party hat
        for i in range(10): fill_rect(50-i//2, 25+i, 50+i//2, 25+i, purple)
        # Confetti
        for _ in range(15):
            import random
            p(random.randint(20,80), random.randint(10,50), random.choice([yellow, neon_green, neon_blue]))
    elif theme == "idea":
        draw_shrimp(50, 60, 1.0)
        # Lightbulb
        fill_rect(45, 15, 55, 25, yellow)
        fill_rect(48, 26, 52, 28, black)
    elif theme == "search":
        draw_shrimp(50, 60, 1.0, r_claw_pos="up")
        # Magnifying glass
        cx, cy = 75, 40
        for y in range(cy-10, cy+11):
            for x in range(cx-10, cx+11):
                if 8**2 <= (x-cx)**2 + (y-cy)**2 <= 10**2: p(x, y, black)
        for i in range(10): p(cx-5-i, cy+5+i, black)
    elif theme == "success":
        # Mountain
        for i in range(40): fill_rect(50-i, 60+i, 50+i, 60+i, "100 100 100")
        draw_shrimp(50, 45, 0.8, r_claw_pos="up")
    elif theme == "collaboration":
        draw_shrimp(35, 60, 0.8, r_claw_pos="cross")
        draw_shrimp(65, 60, 0.8, l_claw_pos="cross")
        # Shake hands (claws)
        fill_rect(45, 60, 55, 65, red)
    elif theme == "zen":
        draw_shrimp(50, 50, 1.0, l_claw_pos="cross", r_claw_pos="cross")
        # Lotus position (bottom fins/legs hint)
        fill_rect(30, 75, 70, 80, light_red)
        # Smoke/aura
        for i in range(3):
            for y in range(10, 30): p(40+i*10 + (y%3), y, "200 200 200")
    elif theme == "music":
        draw_shrimp(50, 55, 1.0, r_claw_pos="up")
        fill_rect(65, 45, 85, 75, "139 69 19") # Guitar
        p(75, 40, black) # Neck
    elif theme == "glitch":
        draw_shrimp(50, 55, 1.0)
        # Glitch lines
        for _ in range(10):
            import random
            y = random.randint(30, 80)
            fill_rect(random.randint(10, 40), y, random.randint(60, 90), y+1, random.choice([neon_blue, "255 0 255"]))

    # Save
    ppm_path = f"{folder}/{name}.ppm"
    png_path = f"{folder}/{name}.png"
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
        ("01_reading", "reading"), ("02_gym", "gym"), ("03_celebration", "celebration"),
        ("04_idea", "idea"), ("05_search", "search"), ("06_success", "success"),
        ("07_collaboration", "collaboration"), ("08_zen", "zen"), ("09_music", "music"),
        ("10_glitch", "glitch")
    ]
    for name, t in themes:
        generate_shrimp_boss_batch3(name, t)
        print(f"Generated {name}")
