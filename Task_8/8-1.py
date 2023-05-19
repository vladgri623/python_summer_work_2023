g = input()
gcode = ''
for i in range(0, len(g)-1, 2):
    if g[i] == 'А' and g[i+1] == 'Г':
        gcode += 'ГА'
    elif g[i] == 'Г' and g[i+1] == 'А':
        gcode += 'АГ'
    elif g[i] == 'Ц' and g[i+1] == 'Т':
        gcode += 'ЦАГТ'
    elif g[i] == 'Т' and g[i+1] == 'Ц':
        gcode += 'ТАГЦ'
    else:
        gcode += g[i] + g[i+1]
print(gcode)
