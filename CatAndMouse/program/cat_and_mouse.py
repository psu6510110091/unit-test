def catAndMouse(x: int, y: int, z: int) -> str:
    distance_a = abs(x - z)
    distance_b = abs(y - z)
    
    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C" if distance_a != 0 else "Cat A and Cat B"