def update_display(display, origional, x, y):
    update_val = 0
    n = len(origional)

    """Check up"""
    if x - 1 > -1 and origional[x - 1][y] == 'X':
        update_val += 1

    """Check right"""
    if y + 1 < n and origional[x][y + 1] == 'X':
        update_val += 1

    """Check down"""
    if x + 1 < n and origional[x + 1][y] == 'X':
        update_val += 1

    """Check left"""
    if y - 1 > -1 and origional[x][y - 1] == 'X':
        update_val += 1

    """Check upright"""
    if x - 1 > -1 and x + 1 < n and origional[x - 1][y + 1] == 'X':
        update_val += 1

    """Check upleft"""
    if x - 1 > -1 and y - 1 > -1 and origional[x - 1][y - 1] == 'X':
        update_val += 1

    """Check downright"""
    if x + 1 < n and y + 1 < n and origional[x + 1][y + 1] == 'X':
        update_val += 1

    """Check downleft"""
    if y - 1 > -1 and x + 1 < n and origional[x + 1][y - 1] == 'X':
        update_val += 1

    display[x][y] = update_val

    return display

   