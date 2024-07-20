# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.
# Se aplicará el siguiente descuento:
# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 

# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

PRECIO_LAMPARA = 800

#Entrada de datos

cantidad = int(input("Ingrese la cantidad de lámparas bajo consumo que desea comprar: "))
marca = input("Ingrese la marca de las lámparas (ArgentinaLuz, FelipeLamparas u otra): ")
precio_total_sin_descuento = PRECIO_LAMPARA * cantidad
precio_final = 0
descuento = 0

if marca == "bajo consumo":
    match cantidad:
        case 5:
            descuento = 30
        case 4:
            descuento = 20
        case 3:
            descuento = 5
        case 2:
            precio_final = precio_total_sin_descuento 
        case 1:
            precio_final = precio_total_sin_descuento 
        case _:
            descuento = 5

elif marca == "ArgentinaLuz":
    match cantidad:
        case 5:
            descuento = 40
        case 4:
            descuento = 25
        case 3:
            descuento = 15
        case _:
            precio_final = precio_total_sin_descuento


elif marca == "FelipeLamparas":
    match cantidad:
        case 5:
            descuento = 30
        case 4:
            descuento = 25
        case 3:
            descuento = 10
        case _:
            precio_final = precio_total_sin_descuento


print(f"Usted ha comprado {cantidad} lamparas de la marca {marca}, siendo un total de {precio_total_sin_descuento}")
descuento_en_pesos = precio_total_sin_descuento * descuento / 100
precio_final = precio_total_sin_descuento - descuento_en_pesos

if precio_final > 4000:
    descuento_extra = precio_final - precio_final*0.5
    if descuento > 0:
        print(f"A usted se le ha aplicado una tasa de descuento del {descuento}% que representa ${descuento_en_pesos}, dando como resultado {precio_final}, que ademas, al haber superado los $4000 se le aplica un descuento del 5% pagando un total de {descuento_extra}")
    else:
        print(f"Usted ha comprado un total de {precio_total_sin_descuento}, que ademas, al haber superado los $4000 se le aplica un descuento del 5% pagando un total de {descuento_extra}")
else:
    if descuento > 0:
        print(f"A usted se le ha aplicado una tasa de descuento del {descuento}%,que representa ${descuento_en_pesos} dando como resultado {precio_final}")
    else:
        print(f"Usted debe pagar un total de {precio_final}, sin goce de descuento")

