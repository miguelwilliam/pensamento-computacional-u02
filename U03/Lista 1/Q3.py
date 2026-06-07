temp, escala = [x for x in input().split(' ')]
temp = float(temp)

if escala.lower() == 'c':
    temp_c = temp
    temp_k = temp+273.15
    temp_f = (temp*9/5)+32
elif escala.lower() == 'k':
    temp_c = temp-273.15
    temp_k = temp
    temp_f = (temp-273.15)*9/5+32
elif escala.lower() == 'f':
    temp_c = (temp-32)*5/9
    temp_k = (temp-32)*5/9+273.15
    temp_f = temp

print(f'Temperatura em Celsius: {temp_c:.2f} °C Temperatura em Fahrenheit: {temp_f:.2f} °F Temperatura em Kelvin: {temp_k:.2f} K')