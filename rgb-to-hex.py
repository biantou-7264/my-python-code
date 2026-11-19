def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex


print(rgb_to_hex(61 + 30, 127 + 30, 255))
