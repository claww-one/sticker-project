import os

def generate_ppm():
    # LINE Standard 370x320
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    # Grid 74x64 (Scale 5x5 per block to maintain chunky pixel style)
    grid_w, grid_h = 74, 64
    bg = "255 255 255"
    pink = "255 200 220" # Body color
    black = "0 0 0"       # Bold outline
    white = "255 255 255" # Eye shine
    blush = "255 150 170" # Cheek blush
    
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # Center position
    cx, cy = 37, 35

    def draw_px(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    # 1. Body Fill (Round/Chubby shape like the reference)
    for y in range(cy-10, cy+20):
        for x in range(cx-18, cx+18):
            if ((x-cx)/17)**2 + ((y-cy)/18)**2 <= 1:
                draw_px(x, y, pink)

    # 2. Ears Fill (Short, Thick, Upright)
    # Left Ear
    for x in range(cx-14, cx-6):
        for y in range(cy-25, cy-8):
            draw_px(x, y, pink)
    # Right Ear
    for x in range(cx+6, cx+14):
        for y in range(cy-25, cy-8):
            draw_px(x, y, pink)

    # 3. BOLD BLACK OUTLINES (The "Sticker" feel)
    # Ears Outline
    ear_outline = [
        # Left
        (cx-15,y) for y in range(cy-24, cy-8)] + [(cx-5,y) for y in range(cy-24, cy-8)] + [(x, cy-25) for x in range(cx-14, cx-6)] + [
        # Right
        (cx+15,y) for y in range(cy-24, cy-8)] + [(cx+5,y) for y in range(cy-24, cy-8)] + [(x, cy-25) for x in range(cx+6, cx+14)
    ]
    # Body Outline
    import math
    for angle in range(0, 360, 1):
        rad = math.radians(angle)
        ox = int(cx + 18 * math.cos(rad))
        oy = int(cy + 19 * math.sin(rad))
        draw_px(ox, oy, black)
        # Connect to ears
        if cy-10 <= oy <= cy-8 and (abs(ox-cx) > 14 or abs(ox-cx) < 6):
             pass # Let ear outlines handle it
             
    for ox, oy in ear_outline: draw_px(ox, oy, black)

    # 4. Face (Simple Kawaii style: . . v)
    # Eyes (Small black dots)
    draw_px(cx-7, cy+2, black); draw_px(cx-7, cy+3, black)
    draw_px(cx+7, cy+2, black); draw_px(cx+7, cy+3, black)
    # Mouth (Small v)
    draw_px(cx, cy+7, black)
    draw_px(cx-1, cy+6, black); draw_px(cx+1, cy+6, black)
    # Blush
    draw_px(cx-11, cy+6, blush); draw_px(cx-12, cy+6, blush)
    draw_px(cx+11, cy+6, blush); draw_px(cx+12, cy+6, blush)

    # Output to PPM with 5x5 scaling
    with open('sticker-project/output/lazy-bunny-1.ppm', 'w') as f:
        f.write(header)
        for y in range(height):
            grid_y = y // 5
            row = []
            for x in range(width):
                grid_x = x // 5
                row.append(data[grid_y][grid_x])
            f.write(" ".join(row) + "\n")

if __name__ == "__main__":
    generate_ppm()
    print("Kawaii Pixel Bunny (Sticker Style) generated.")
