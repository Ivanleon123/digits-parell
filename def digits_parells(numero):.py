    def digits_parells(numero):
        """Retorna una llista de dígits parells del número."""
        parells = []
        for digit in str(numero):
            if int(digit) % 2 == 0:
                parells.append(digit)
        return parells

    def main():
        # Demanar un número a l'usuari
        numero = int(input("Introdueix un número: "))

        # Obtenir els dígits parells
        parells = digits_parells(numero)

        # Mostrar els dígits parells
        if parells:
            print(f"Els dígits parells de {numero} són: {', '.join(parells)}")
        else:
            print(f"No hi ha dígits parells en el número {numero}.")

    # Executar el programa
    if __name__ == "__main__":
        main()