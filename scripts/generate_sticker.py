import os

def generate_ppm():
    # LINE Sticker standard size: 370 x 320
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    # 37x32 grid (10px per cell)
    grid_w, grid_h = 37, 32
    
    # Colors
    bg = "255 255 255"      # White background (for preview)
    bunny = "255 255 255"   # White fur
    outline = "0 0 0"       # Black outline (Bold)
    eye = "0 0 0"
    nose = "255 192 203"
    ear_inner = "255 235 235"

    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    off_x, off_y = 6, 10
    
    # 1. Draw Body Fill
    for x in range(3, 23):
        for y in range(5, 13):
            data[off_y + y][off_x + x] = bunny

    # 2. Draw Ears Fill (Droopy)
    for x in range(0, 5):
        for y in range(5, 11):
            data[off_y + y][off_x + x] = bunny
            
    # 3. Draw BOLD Black Outlines
    # Body Horizontal
    for x in range(3, 23):
        data[off_y + 4][off_x + x] = outline
        data[off_y + 13][off_x + x] = outline
    # Body Vertical
    for y in range(5, 13):
        data[off_y + y][off_x + 23] = outline
    
    # Ears Outlines
    for x in range(0, 4):
        data[off_y + 4][off_x + x] = outline
        data[off_y + 11][off_x + x] = outline
    for y in range(5, 11):
        data[off_y + y][off_x - 1] = outline
        
    # Nose
    data[off_y + 10][off_x + 18] = nose
    
    # Eyes (Lazy/Sleeping)
    data[off_y + 8][off_x + 15] = eye
    data[off_y + 8][off_x + 16] = eye
    data[off_y + 8][off_x + 19] = eye
    data[off_y + 8][off_x + 20] = eye

    # 4. Scale up to 370x320
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
    print("Sticker with BOLD OUTLINE generated.")
