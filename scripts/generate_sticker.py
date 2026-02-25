import os

def generate_ppm():
    # 畫布尺寸 370x320
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    # 使用更高解析度的網格 (185x160)，每格 2px，讓線條更細緻
    grid_w, grid_h = 185, 160
    bg = "255 255 255"
    white = "255 255 255"
    black = "0 0 0"
    pink = "255 180 200"
    shadow = "230 230 230"

    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # 兔子的精細座標 (中心點)
    cx, cy = 92, 80
    
    def draw_rect(x, y, w, h, color):
        for i in range(x, x+w):
            for j in range(y, y+h):
                if 0 <= i < grid_w and 0 <= j < grid_h:
                    data[j][i] = color

    # 1. 身體陰影 (讓兔子有立體感)
    draw_rect(cx-45, cy+5, 90, 35, shadow)
    # 2. 身體主體
    draw_rect(cx-48, cy, 96, 35, white)
    # 3. 身體描邊 (精細黑色 1格寬)
    # 上下邊
    for x in range(cx-48, cx+48):
        data[cy-1][x] = black
        data[cy+35][x] = black
    # 左右邊
    for y in range(cy, cy+35):
        data[y][cx-49] = black
        data[y][cx+48] = black

    # 4. 頭部 (圓潤一點)
    draw_rect(cx+20, cy-15, 40, 40, white)
    # 頭部描邊
    for x in range(cx+20, cx+60):
        data[cy-16][x] = black
        data[cy+25][x] = black
    for y in range(cy-15, cy+25):
        data[y][cx+19] = black
        data[y][cx+60] = black

    # 5. 垂耳 (左)
    draw_rect(cx+10, cy-5, 12, 35, white)
    for y in range(cy-5, cy+30):
        data[y][cx+9] = black
        data[y][cx+22] = black
    for x in range(cx+10, cx+22):
        data[cy-6][x] = black
        data[cy+30][x] = black

    # 6. 表情 (更細緻的瞇瞇眼)
    data[cy+5][cx+40] = black
    data[cy+5][cx+41] = black
    data[cy+5][cx+42] = black
    data[cy+5][cx+50] = black
    data[cy+5][cx+51] = black
    data[cy+5][cx+52] = black
    
    # 小鼻子
    data[cy+12][cx+46] = pink
    
    # 7. 短尾巴
    draw_rect(cx-55, cy+15, 10, 10, white)
    for x in range(cx-55, cx-45):
        data[cy+14][x] = black
        data[cy+25][x] = black
    for y in range(cy+15, cy+25):
        data[y][cx-56] = black

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
    print("Sophisticated Pixel Bunny generated.")
