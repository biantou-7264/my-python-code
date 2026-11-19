def hex_to_rgb(hex):
    rh = hex[1:3]
    gh = hex[3:5]
    bh = hex[5:7]
    r = int(rh, 16)
    g = int(gh, 16)
    b = int(bh, 16)
    return r, g, b


print(hex_to_rgb('#3D7fff'))
