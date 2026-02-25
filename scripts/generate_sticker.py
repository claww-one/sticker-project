import os

def generate_ppm():
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    grid_w, grid_h = 185, 160
    bg = "255 255 255"
    white = "255 255 255"
    black = "0 0 0"
    pink = "255 180 200"
    
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # 重新設定中心點
    cx, cy = 92, 90 

    def draw_pixel(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    def draw_fill(x1, y1, x2, y2, color):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                draw_pixel(i, j, color)

    # 1. 兔子的立耳 (放在頭頂上方，這才像兔子)
    # 左耳
    draw_fill(cx-12, cy-45, cx-2, cy-15, white)
    for y in range(cy-45, cy-14): draw_pixel(cx-13, y, black); draw_pixel(cx-1, y, black)
    for x in range(cx-12, cx-1): draw_pixel(x, cy-46, black)
    # 右耳
    draw_fill(cx+2, cy-45, cx+12, cy-15, white)
    for y in range(cy-45, cy-14): draw_pixel(cx+1, y, black); draw_pixel(cx+13, y, black)
    for x in range(cx+2, cx+13): draw_pixel(x, cy-46, black)

    # 2. 圓圓的腦袋 (放在耳朵下方，不再是長方形)
    # 填充一個接近圓形的區域
    draw_fill(cx-18, cy-14, cx+18, cy+20, white)
    # 腦袋描邊
    for x in range(cx-12, cx+13): draw_pixel(x, cy-15, black); draw_pixel(x, cy+21, black)
    for y in range(cy-9, cy+16): draw_pixel(cx-19, y, black); draw_pixel(cx+19, y, black)
    # 切角讓頭變圓
    draw_pixel(cx-18, cy-13, black); draw_pixel(cx-17, cy-14, black); draw_pixel(cx-16, cy-15, black)
    draw_pixel(cx+18, cy-13, black); draw_pixel(cx+17, cy-14, black); draw_pixel(cx+16, cy-15, black)

    # 3. 懶散的身體 (側躺在頭的左側，形成 L 型姿態)
    draw_fill(cx-60, cy+5, cx-19, cy+20, white)
    for x in range(cx-55, cx-19): draw_pixel(x, cy+4, black); draw_pixel(x, cy+21, black)
    for y in range(cy+9, cy+16): draw_pixel(cx-61, y, black)
    
    # 4. 五官 (放在圓臉的正中心)
    # 瞇瞇眼
    draw_pixel(cx-8, cy+2, black); draw_pixel(cx-7, cy+2, black)
    draw_pixel(cx+7, cy+2, black); draw_pixel(cx+8, cy+2, black)
    # 小鼻子 (要在眼睛下方，不能長在臉頰)
    draw_pixel(cx, cy+8, pink)

    # 5. 圓尾巴
    draw_fill(cx-70, cy+8, cx-61, cy+17, white)
    for x in range(cx-68, cx-63): draw_pixel(x, cy+7, black); draw_pixel(x, cy+18, black)
    for y in range(cy+10, cy+15): draw_pixel(cx-71, y, black)

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
    print("Real Bunny Redux generated.")
