def Staircase(step,display='#'):
    text = ''
    if 0 < step <= 30:
        for i in range(1, step + 1):
            text += (' ' * ( step-i ) + display * i + ('\n' if step > 1 else ''))
    return text