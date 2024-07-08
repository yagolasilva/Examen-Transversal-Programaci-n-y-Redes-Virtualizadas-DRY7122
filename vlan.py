# vlan_check.py

vlan_number = int(input("Introduce el número de VLAN: "))

if 1 <= vlan_number <= 1005:
    print("La VLAN está en el rango normal.")
elif 1006 <= vlan_number <= 4094:
    print("La VLAN está en el rango extendido.")
else:
    print("Número de VLAN no válido.")
