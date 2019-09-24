package main

import (
	"fmt"
	"sort"
)

func main() {
	lista := []int{-5, -4, -3, -2, -1, 0, 1, 2}
	diferenca := Solution(lista)
	fmt.Println(diferenca)
}

func Solution(A []int) int {
	ordenada := A
	sort.Ints(ordenada)
	alvo := Somatorio(ordenada[0], ordenada[len(ordenada) - 1]) / 2
	dif := buscaBinaria(ordenada, alvo)
	//esquerda, direita := Divide(ordenada)
	//sumEsq := Somatorio(esquerda[0], esquerda[len(esquerda) - 1])
	//sumDir := Somatorio(direita[0], direita[len(direita) - 1])
	//dif := sumEsq - sumDir
	//if dif < 0 {dif *= -1}
	return dif
}

func buscaBinaria(seq []int, alvo int) int {
	E := 0
	D := len(seq) - 1
	for E <= D {
		meio := (E + D) / 2
		somaMeio := Somatorio(seq[0], seq[meio])
		somaMeioMais := Somatorio(seq[0], seq[meio] + 1)
		if somaMeio < alvo && somaMeioMais > alvo {
			return somaMeioMais - somaMeio
		} else if somaMeio < alvo {
			E = meio + 1
		} else {
			D = meio - 1
		}
	}
	return 0
}

func Somatorio(inicio int, fim int) int {
	termoInicio := 1
	termoFim := 1
	if inicio < 0 {termoInicio *= -1}
	if fim < 0 {termoFim *= -1}
	somatorio := (fim*(fim + termoFim)/2) - (inicio*(inicio + termoInicio)/2)
	return somatorio
}
