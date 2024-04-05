def check_vowels():
    name_string = input("Ingrese un nombre")
    name = name_string.lower()

    print(f"contiene a:{"a" in name}")
    print(f"contiene e:{"e" in name}")
    print(f"contiene i:{"i" in name}")
    print(f"contiene o:{"o" in name}")
    print(f"contiene u:{"u" in name}")

check_vowels()
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
