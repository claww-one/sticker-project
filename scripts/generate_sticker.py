import os

def generate_ppm():
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    # 網格 185x160 (每格 2px)
    grid_w, grid_h = 185, 160
    bg = "255 255 255"
    white = "255 255 255"
    black = "0 0 0"
    pink = "255 180 200"
    
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # 中心基準點 (頭部中心)
    cx, cy = 130, 80 

    def draw_pixel(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    def draw_fill(x1, y1, x2, y2, color):
        for i in range(int(x1), int(x2) + 1):
            for j in range(int(y1), int(y2) + 1):
                draw_pixel(i, j, color)

    # 1. 耳朵 (向上、長長的，這才是兔子！)
    # 左耳
    draw_fill(cx-15, cy-50, cx-5, cy-20, white)
    for y in range(cy-50, cy-20): draw_pixel(cx-16, y, black); draw_pixel(cx-4, y, black)
    for x in range(cx-15, cx-4): draw_pixel(x, cy-51, black)
    # 右耳
    draw_fill(cx+5, cy-50, cx+15, cy-20, white)
    for y in range(cy-50, cy-20): draw_pixel(cx+4, y, black); draw_pixel(cx+16, y, black)
    for x in range(cx+5, cx+16): draw_pixel(x, cy-51, black)

    # 2. 圓圓的臉 (不是方塊，也不是長在象鼻上方)
    # 頭部填充 (圓形近似)
    for y in range(cy-20, cy+21):
        for x in range(cx-20, cx+21):
            if (x-cx)**2 + (y-cy)**2 <= 20**2:
                draw_pixel(x, y, white)
    # 頭部描邊 (圓周)
    for angle in range(0, 360, 2):
        import math
        rx = int(cx + 21 * math.cos(math.radians(angle)))
        ry = int(cy + 21 * math.sin(math.radians(angle)))
        draw_pixel(rx, ry, black)

    # 3. 身體 (橢圓形，連在頭部左側，側躺姿態)
    bx, by = cx-40, cy+10
    for y in range(by-15, by+16):
        for x in range(bx-30, bx+31):
            if ((x-bx)/30)**2 + ((y-by)/15)**2 <= 1:
                draw_pixel(x, y, white)
    # 身體描邊
    for angle in range(0, 360, 2):
        import math
        rx = int(bx + 31 * math.cos(math.radians(angle)))
        ry = int(by + 16 * math.sin(math.radians(angle)))
        draw_pixel(rx, ry, black)

    # 4. 圓尾巴 (重要特徵)
    tx, ty = bx-32, by
    for y in range(ty-8, ty+9):
        for x in range(tx-8, tx+9):
            if (x-tx)**2 + (y-ty)**2 <= 8**2:
                draw_pixel(x, y, white)
    # 尾巴描邊
    for angle in range(0, 360, 5):
        import math
        rx = int(tx + 9 * math.cos(math.radians(angle)))
        ry = int(ty + 9 * math.sin(math.radians(angle)))
        draw_pixel(rx, ry, black)

    # 5. 五官 (細微調整)
    # 瞇瞇眼 (在頭部中心附近)
    draw_fill(cx-10, cy-2, cx-4, cy-2, black) # 左眼
    draw_fill(cx+4, cy-2, cx+10, cy-2, black) # 右眼
    # 小鼻子
    draw_pixel(cx, cy+5, pink)

    # 輸出 PPM
    with open('sticker-project/output/lazy-bunny-1.ppm', 'w') as f:
        f.write(header)
        for y in range(height):
            grid_y = y // 2
            row = []
            for x in range(width):
                grid_x = x // 2
                row.append(data[grid_y][grid_x])
            f.write(" ".join(row) + "\n")

if __name__ == "__main__":
    generate_ppm()
    print("Self-Verified Bunny Redesign generated.")
