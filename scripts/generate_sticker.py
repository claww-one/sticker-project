import os

def generate_ppm():
    # LINE Standard 370x320
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    # Grid 37x32 (10px per block) - Pure Chunky Style
    grid_w, grid_h = 37, 32
    bg = "255 255 255"
    pink = "255 192 203" # Pink bunny
    black = "0 0 0"       # Thick black outline
    white = "255 255 255"
    blush = "255 120 150"

    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # Base coordinates
    cx, cy = 18, 16

    def draw_block(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    # --- BODY (Chunky Circle/Blob) ---
    # Fill
    for y in range(cy-5, cy+7):
        for x in range(cx-8, cx+9):
            if ((x-cx)/8)**2 + ((y-cy)/6)**2 <= 1:
                draw_block(x, y, pink)

    # Outline (Manual chunky placement)
    body_outline = [
        (10,12),(11,11),(12,11),(13,10),(14,10),(15,10),(16,10),(17,10),(18,10),(19,10),(20,10),(21,10),(22,11),(23,11),(24,12),(25,13),
        (26,14),(26,15),(26,16),(26,17),(26,18),(25,19),(24,20),(23,21),(22,22),(21,22),(20,22),(19,22),(18,22),(17,22),(16,22),(15,22),(14,22),
        (13,21),(12,20),(11,19),(10,18),(10,17),(10,16),(10,15),(10,14),(10,13)
    ]
    for x, y in body_outline: draw_block(x, y, black)

    # --- EARS (Classic Rabbit Pillars) ---
    # Left Ear
    draw_block(13, 6, black); draw_block(14, 6, black); draw_block(15, 6, black)
    draw_block(12, 7, black); draw_block(12, 8, black); draw_block(12, 9, black); draw_block(12, 10, black)
    draw_block(16, 7, black); draw_block(16, 8, black); draw_block(16, 9, black)
    for y in range(7, 10): draw_block(13, y, pink); draw_block(14, y, pink); draw_block(15, y, pink)
    
    # Right Ear
    draw_block(21, 6, black); draw_block(22, 6, black); draw_block(23, 6, black)
    draw_block(20, 7, black); draw_block(20, 8, black); draw_block(20, 9, black); draw_block(20, 10, black)
    draw_block(24, 7, black); draw_block(24, 8, black); draw_block(24, 9, black)
    for y in range(7, 10): draw_block(21, y, pink); draw_block(22, y, pink); draw_block(23, y, pink)

    # --- FACE (. . v) ---
    draw_block(14, 15, black) # Left Eye
    draw_block(22, 15, black) # Right Eye
    draw_block(18, 17, black) # Nose/Mouth
    
    # Blush
    draw_block(12, 16, blush); draw_block(24, 16, blush)

    # Output to PPM with 10x10 scaling
    with open('sticker-project/output/lazy-bunny-1.ppm', 'w') as f:
        f.write(header)
        for y in range(height):
            grid_y = y // 10
            row = []
            for x in range(width):
                grid_x = x // 10
                row.append(data[grid_y][grid_x])
            f.write(" ".join(row) + "\n")

if __name__ == "__main__":
    generate_ppm()
    print("ULTRA CHUNKY KAWAII BUNNY generated.")
