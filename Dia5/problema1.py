def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return suma - max(num1, num2, num3) - min(num1, num2, num3)

print(devolver_distintos(1, 2, 3)) # 2
print(devolver_distintos(1, 2, 10)) # 2
print(devolver_distintos(1, 2, 15)) # 15