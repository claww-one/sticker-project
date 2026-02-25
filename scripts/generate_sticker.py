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
    
    cx, cy = 92, 90

    def draw_pixel(x, y, color):
        if 0 <= x < grid_w and 0 <= y < grid_h:
            data[y][x] = color

    def draw_fill_rect(x1, y1, x2, y2, color):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                draw_pixel(i, j, color)

    # 1. 身體 (橢圓形處理)
    draw_fill_rect(cx-50, cy+5, cx+30, cy+35, white) # 身體主體
    # 身體描邊 (切角模擬圓弧)
    for x in range(cx-48, cx+28): 
        draw_pixel(x, cy+4, black)
        draw_pixel(x, cy+36, black)
    for y in range(cy+6, cy+34):
        draw_pixel(cx-51, y, black)
        draw_pixel(cx+31, y, black)

    # 2. 圓潤的腦袋 (重點優化：切角技術)
    # 腦袋填充
    draw_fill_rect(cx+32, cy-15, cx+68, cy+21, white)
    # 腦袋描邊 (手動切掉四個角讓它變圓)
    # 頂邊與底邊
    for x in range(cx+36, cx+64):
        draw_pixel(x, cy-16, black) # 頂
        draw_pixel(x, cy+22, black) # 底
    # 左右邊
    for y in range(cy-11, cy+17):
        draw_pixel(cx+31, y, black) # 左
        draw_pixel(cx+69, y, black) # 右
    # 斜角 (切角)
    corner_pts = [
        (cx+35, cy-15), (cx+34, cy-14), (cx+33, cy-13), (cx+32, cy-12), # 左上
        (cx+65, cy-15), (cx+66, cy-14), (cx+67, cy-13), (cx+68, cy-12), # 右上
        (cx+35, cy+21), (cx+34, cy+20), (cx+33, cy+19), (cx+32, cy+18), # 左下
        (cx+65, cy+21), (cx+66, cy+20), (cx+67, cy+19), (cx+68, cy+18)  # 右下
    ]
    for px, py in corner_pts: draw_pixel(px, py, black)

    # 3. 軟趴趴的垂耳 (增加一點弧度)
    # 耳朵 1
    draw_fill_rect(cx+48, cy+15, cx+58, cy+55, white)
    for y in range(cy+16, cy+54):
        draw_pixel(cx+47, y, black)
        draw_pixel(cx+59, y, black)
    for x in range(cx+48, cx+59): draw_pixel(x, cy+55, black)

    # 4. 五官 (微調位置)
    draw_pixel(cx+52, cy+3, black); draw_pixel(cx+53, cy+3, black) # 左眼
    draw_pixel(cx+62, cy+3, black); draw_pixel(cx+63, cy+3, black) # 右眼
    draw_pixel(cx+58, cy+9, pink) # 小鼻子

    # 5. 圓尾巴 (切角圓化)
    draw_fill_rect(cx-58, cy+15, cx-48, cy+25, white)
    for x in range(cx-56, cx-50): draw_pixel(x, cy+14, black); draw_pixel(x, cy+26, black)
    for y in range(cy+16, cy+24): draw_pixel(cx-59, y, black); draw_pixel(cx-47, y, black)

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
    print("Rounded Head Bunny generated.")
