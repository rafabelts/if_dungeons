def renderTextCenteredAt(text, font, color, x, y, screen, allowed_width):
    # Split the text into words
    words = text.split()

    # Construct lines of those word
    lines = []
    while len(words) > 0:
        # Get words as to fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # Add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # Render each line below the last, so have to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, color)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh

