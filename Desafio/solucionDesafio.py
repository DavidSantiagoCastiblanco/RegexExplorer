import re 

texto = input("\ningresa un texto de gusto o preferencia:")


patron_enteros = r"-?\b\d+\b"
patron_flotante = r"-?\b\d+\.\d+\b"
patron_booleans = r"\b(True|False)\b"
patron_string = r'"(.*?)"'
patron_listas = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"

enteros = re.findall(patron_enteros, texto)
flotantes = re.findall(patron_flotante, texto)
booleans = re.findall(patron_booleans, texto, re.IGNORECASE)
strings = re.findall(patron_string, texto)
listas = re.findall(patron_listas, texto)

print("Enteros encontrados:", enteros)
print("Flotantes encontrados:", flotantes)
print("Booleanos encontrados:", booleans)
print("Strings encontrados:", strings)
print("Listas encontradas:", listas)