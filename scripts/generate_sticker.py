import os

def generate_ppm():
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    grid_w, grid_h = 185, 160
    bg = "255 255 255"
    white = "255 255 255"
    black = "0 0 0"
    pink = "255 180 200"
    shadow = "220 220 220"

    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    cx, cy = 92, 100 # 下移一點給耳朵空間

    def draw_rect(x, y, w, h, color):
        for i in range(x, x+w):
            for j in range(y, y+h):
                if 0 <= i < grid_w and 0 <= j < grid_h:
                    data[j][i] = color

    def draw_outline(x, y, w, h):
        for i in range(x, x+w):
            if 0 <= i < grid_w:
                if 0 <= y < grid_h: data[y][i] = black
                if 0 <= y+h-1 < grid_h: data[y+h-1][i] = black
        for j in range(y, y+h):
            if 0 <= j < grid_h:
                if 0 <= x < grid_w: data[j][x] = black
                if 0 <= x+w-1 < grid_w: data[j][x+w-1] = black

    # 1. 橢圓形身體 (攤平感)
    draw_rect(cx-50, cy, 100, 30, white)
    draw_outline(cx-50, cy, 100, 30)
    
    # 2. 圓圓的頭 (連在身體右側)
    draw_rect(cx+30, cy-15, 35, 35, white)
    draw_outline(cx+30, cy-15, 35, 35)
    
    # 3. 兔子的核心特徵：長耳朵 (一對，垂下來)
    # 耳朵1 (在頭後方)
    draw_rect(cx+45, cy+5, 10, 40, white)
    draw_outline(cx+45, cy+5, 10, 40)
    # 耳朵2 (在頭前方，遮住一點臉)
    draw_rect(cx+35, cy+10, 10, 45, white)
    draw_outline(cx+35, cy+10, 10, 45)

    # 4. 懶散的五官
    # 瞇瞇眼 (一條線)
    draw_rect(cx+50, cy+5, 8, 1, black)
    # 小鼻子 (粉紅色 V 字感)
    data[cy+12][cx+58] = pink
    data[cy+13][cx+58] = pink
    
    # 5. 縮起來的小手和小腳 (兔子的特徵)
    # 前肢
    draw_rect(cx+10, cy+25, 10, 8, white)
    draw_outline(cx+10, cy+25, 10, 8)
    # 後肢 (縮在屁股後面)
    draw_rect(cx-55, cy+20, 12, 10, white)
    draw_outline(cx-55, cy+20, 12, 10)
    
    # 6. 圓尾巴 (重要特徵)
    draw_rect(cx-62, cy+5, 12, 12, white)
    draw_outline(cx-62, cy+5, 12, 12)

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
    print("Real-look Lazy Bunny generated.")
