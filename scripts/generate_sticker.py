import os

def generate_ppm():
    # Basic PPM (P3) generator to create a 370x320 image
    # We'll generate a 37x32 "pixel" grid and scale it up or just use raw pixels.
    # To keep it simple and ensure no dependencies, we create a simple pattern.
    
    width, height = 370, 320
    header = f"P3\n{width} {height}\n255\n"
    
    pixels = []
    # Fill with "transparent" replacement (white for PPM, as PPM has no alpha)
    # We will use this to verify the composition first.
    bg = "255 255 255" 
    bunny = "255 255 255"
    outline = "211 211 211"
    eye = "0 0 0"
    nose = "255 192 203"

    # 37x32 grid logic
    grid_w, grid_h = 37, 32
    data = [[bg for _ in range(grid_w)] for _ in range(grid_h)]
    
    off_x, off_y = 5, 12
    
    # Draw Bunny Body
    for x in range(2, 22):
        for y in range(4, 12):
            data[off_y + y][off_x + x] = bunny
            
    # Ears
    for x in range(0, 4):
        for y in range(4, 10):
            data[off_y + y][off_x + x] = bunny

    # Eyes
    data[off_y + 7][off_x + 14] = eye
    data[off_y + 7][off_x + 15] = eye
    data[off_y + 7][off_x + 18] = eye
    data[off_y + 7][off_x + 19] = eye
    
    # Nose
    data[off_y + 9][off_x + 17] = nose

    # Scaling up to 370x320
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
    print("PPM generated.")
