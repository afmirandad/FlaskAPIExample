#!/bin/bash

# Script para llenar la base de datos con 20 electrodomésticos
# Uso: ./llenarelectrodomesticos.sh
# Nota: Asegúrate de que el servidor esté corriendo en localhost:6060

BASE_URL="http://localhost:6060"
ENDPOINT="${BASE_URL}/electrodomesticos/"

echo "=========================================="
echo "  Llenando base de datos con electrodomésticos"
echo "=========================================="
echo ""

# Función para crear un electrodoméstico
create_electrodomestico() {
    local marca="$1"
    local modelo="$2"
    local tipo="$3"
    local precio="$4"
    local clase_energetica="$5"
    local en_stock="$6"
    
    echo "Creando: $marca $modelo ($tipo) - \$$precio"
    
    curl -X POST "$ENDPOINT" \
        -H "Content-Type: application/json" \
        -d "{
            \"marca\": \"$marca\",
            \"modelo\": \"$modelo\",
            \"tipo\": \"$tipo\",
            \"precio\": $precio,
            \"clase_energetica\": \"$clase_energetica\",
            \"en_stock\": $en_stock
        }" \
        -s -w "\nCódigo HTTP: %{http_code}\n" | head -n 3
    
    echo ""
}

# Neveras (5 unidades)
create_electrodomestico "Samsung" "RF28R7351SG" "Nevera" 1299.99 "A++" true
create_electrodomestico "LG" "GBB72MCUFN" "Nevera" 899.50 "A+" true
create_electrodomestico "Bosch" "KGN39VIEA" "Nevera" 1150.00 "A++" true
create_electrodomestico "Whirlpool" "WQ9E1L" "Nevera" 749.99 "A+" false
create_electrodomestico "Siemens" "KG39NVIEA" "Nevera" 1089.00 "A++" true

# Lavadoras (5 unidades)
create_electrodomestico "Samsung" "WW90T554DAW" "Lavadora" 549.99 "A+++" true
create_electrodomestico "LG" "F4WV5009S2W" "Lavadora" 479.00 "A+++" true
create_electrodomestico "Bosch" "WAU28S40ES" "Lavadora" 599.99 "A+++" true
create_electrodomestico "Balay" "3TS873B" "Lavadora" 429.00 "A++" false
create_electrodomestico "Indesit" "MTWE91483WK" "Lavadora" 349.99 "A++" true

# Lavavajillas (3 unidades)
create_electrodomestico "Bosch" "SMV46KX00E" "Lavavajillas" 649.00 "A++" true
create_electrodomestico "Siemens" "SN658X06TE" "Lavavajillas" 799.99 "A+++" true
create_electrodomestico "Candy" "CDPN4D620PW" "Lavavajillas" 399.00 "A+" true

# Hornos (3 unidades)
create_electrodomestico "Bosch" "HBG6764S6" "Horno" 749.99 "A+" true
create_electrodomestico "Teka" "HSB630P" "Horno" 459.00 "A" true
create_electrodomestico "AEG" "BPE742320M" "Horno" 889.00 "A++" false

# Microondas (2 unidades)
create_electrodomestico "Samsung" "MC28H5013AW" "Microondas" 199.99 "B" true
create_electrodomestico "Panasonic" "NN-SD27HSBPQ" "Microondas" 149.00 "B" true

# Secadoras (2 unidades)
create_electrodomestico "Samsung" "DV90T6240LH" "Secadora" 599.99 "A++" true
create_electrodomestico "Bosch" "WTW87641ES" "Secadora" 749.00 "A+++" false

echo "=========================================="
echo "  Proceso completado"
echo "=========================================="
echo ""
echo "Para verificar los electrodomésticos creados, ejecuta:"
echo "curl -X GET ${BASE_URL}/electrodomesticos/"
echo ""
