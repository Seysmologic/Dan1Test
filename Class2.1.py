
import math

geom_object = input('Enter the object type ').capitalize()

match geom_object:
    case 'Circle':
        rad = int(input('Enter radius ').strip())
        area_circ = math.pi*math.pow(rad, 2)
        print(f'Area of a circle is {area_circ}')
        if area_circ > 100:
            print('BIG')
        else:
            print('SMALL')
    case 'Square':
        sq_side = int(input('Enter square side ').strip())
        area_square = math.pow(sq_side, 2)
        print(f'Area of a square is {area_square}')
        if area_square > 100:
            print('BIG')
        else:
            print('SMALL')
    case 'Rectangle':
        side_hei = int(input('Enter rectangle height ').strip())
        side_len = int(input('Enter rectangle length ').strip())
        area_rect = side_hei*side_hei
        print(f'Area of a rectangle is {area_rect}')
        if area_rect > 100:
            print('BIG')
        else:
            print('SMALL')
    case 'Triangle':
        tri_side_a = int(input('Enter triangle side A ').strip())
        tri_side_b = int(input('Enter triangle side B ').strip())
        tri_side_c = int(input('Enter triangle side C ').strip())
        area_tri = tri_side_a * tri_side_b * tri_side_c
        if area_tri > 100:
            print('BIG')
        else:
            print('SMALL')
        print(f'Area of a triangle is {area_tri}')