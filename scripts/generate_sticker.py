import os

def generate_ppm():
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    grid_w, grid_h = 185, 160
    bg = "255 255 255"
    white = "255 255 255"
    black = "0 0 0"
    pink = "255 180 200"
    shadow = "240 240 240"

    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    # 中心點下移，把空間讓給向上的耳朵
    cx, cy = 92, 110 

    def draw_pixel(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    def draw_fill(x1, y1, x2, y2, color):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                draw_pixel(i, j, color)

    # 1. 兔子的靈魂：一對長長的立耳 (向上且稍微撇開，這才像兔子)
    # 左耳
    draw_fill(cx+35, cy-60, cx+45, cy-15, white)
    for y in range(cy-59, cy-15): draw_pixel(cx+34, y, black); draw_pixel(cx+46, y, black)
    for x in range(cx+35, cx+46): draw_pixel(x, cy-60, black)
    # 右耳
    draw_fill(cx+55, cy-50, cx+65, cy-15, white)
    for y in range(cy-49, cy-15): draw_pixel(cx+54, y, black); draw_pixel(cx+66, y, black)
    for x in range(cx+55, cx+66): draw_pixel(x, cy-50, black)

    # 2. 圓圓的小臉 (連接耳朵下方)
    draw_fill(cx+30, cy-15, cx+70, cy+25, white)
    # 臉部圓潤化描邊
    for x in range(cx+35, cx+66): draw_pixel(x, cy-16, black); draw_pixel(x, cy+26, black)
    for y in range(cy-10, cy+21): draw_pixel(cx+29, y, black); draw_pixel(cx+71, y, black)
    # 切角
    draw_pixel(cx+30, cy-13, black); draw_pixel(cx+31, cy-14, black); draw_pixel(cx+32, cy-15, black)
    draw_pixel(cx+68, cy-15, black); draw_pixel(cx+69, cy-14, black); draw_pixel(cx+70, cy-13, black)

    # 3. 縮起來的身體 (側躺感，不能太長像象鼻)
    draw_fill(cx-30, cy+5, cx+35, cy+30, white)
    for x in range(cx-25, cx+35): draw_pixel(x, cy+4, black); draw_pixel(x, cy+31, black)
    for y in range(cy+10, cy+25): draw_pixel(cx-31, y, black)

    # 4. 懶散五官 (微調位置)
    # 瞇瞇眼 (一條線)
    draw_pixel(cx+40, cy+5, black); draw_pixel(cx+41, cy+5, black); draw_pixel(cx+42, cy+5, black)
    draw_pixel(cx+58, cy+5, black); draw_pixel(cx+59, cy+5, black); draw_pixel(cx+60, cy+5, black)
    # 鼻子
    draw_pixel(cx+50, cy+12, pink)

    # 5. 圓尾巴
    draw_fill(cx-42, cy+10, cx-32, cy+20, white)
    for x in range(cx-40, cx-34): draw_pixel(x, cy+9, black); draw_pixel(x, cy+21, black)
    for y in range(cy+12, cy+18): draw_pixel(cx-43, y, black)

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
    print("Proper Bunny (Not Elephant) generated.")
