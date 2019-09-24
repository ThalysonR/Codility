def CalculateJmpConta(posicao_inicial, destino, distancia_pulo):
    if posicao_inicial < destino:
        pulos, resto = divmod((destino - posicao_inicial), distancia_pulo)
        if resto > 0:
            pulos += 1
        return pulos
    return 0


if __name__ == '__main__':
    pulos = CalculateJmpConta(10, 85, 70)
    print(pulos)
