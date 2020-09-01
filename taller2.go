package main

import (
	"math/rand"
	"os"
	"strconv"
	"time"
)

type mapa struct {
	barcos    int
	jugadores int
}

type barco struct {
	id         int
	ataque     bool
	horizontal bool
	numero     int
	vida       int
}

func inicializar_barco() barco {

	m := barco{
		horizontal: true,
		id:         1,
		numero:     1,
	}
	return m
}

/*
func realizar_movimiento(matriz [][]barco, x int, y int){
	if matriz [x][y]barco == -1{
		return "fallido"
	}else if matriz [x][y]barco == '*' && matriz [x][y]barco == '$' {
		return "Intente nuevamente"
	}else{
		return "bombazo"
	}
}*/

/*func movimiento_maquina(matriz [][]barco) {

	for true {
		for i := 0; i < len(matriz); i++ {
			rand.Seed(time.Now().UnixNano())
			print(len(matriz))
			s1 := rand.Intn(len(matriz) - 2)
			s2 := rand.Intn(len(matriz) - 2)
		}
	}
}*/

func insert_barcos_matriz(vector_barco []barco, matriz [][]barco, posicion int) { //funcion para insertar barcos
	//vector_barco[1] = append(vector_barco, matriz[3][5])
	for i := posicion; i < len(vector_barco); i++ {
		rand.Seed(time.Now().UnixNano())
		s1 := rand.Intn(len(matriz) - 2)
		s2 := rand.Intn(len(matriz) - 2)
		var aux barco
		aux.id = 1
		if matriz[s1][s2].id != 0 { // casilla ocupada
			for {
				x := rand.Intn(len(matriz) - 2)
				y := rand.Intn(len(matriz) - 2)
				if matriz[x][y].id == 0 && matriz[x][y+1].id == 0 && matriz[x][y+2].id == 0 {
					s1 = x
					s2 = y
					break
				}
			}
			for k := 0; k < 3; k++ {
				matriz[s1][s2+k] = vector_barco[i]
			}
		} else if matriz[s1][s2].id == 0 { // caso cuando las casillas esten desocupadas
			if matriz[s1][s2+1].id == 0 && matriz[s1][s2+2].id == 0 {
				for k := 0; k < 3; k++ {
					matriz[s1][s2+k] = vector_barco[i]
				}
				posicion = posicion + 1
			} else if matriz[s1+1][s2].id == 0 && matriz[s1+1][s2].id == 0 {
				for k := 0; k < 3; k++ {
					matriz[s1+k][s2] = vector_barco[i]
					matriz[s1][s2].horizontal = false
					posicion = posicion + 1
				}
			} else {
				print("asdasd")
			}
		} else {
			print("caso que nose")
		}
	}
}

func verificarTablero(mp [][]barco) bool {

	//var contador int

	//contador = 0

	for i := 0; i < len(mp); i++ {
		print("\n ", i, " ")
		for j := 0; j < len(mp); j++ {

			if mp[i][j].numero == 0 { // si no hay barcos
				print("\n")
			} else if mp[i][j].vida == 3 { // barco caido
				print("\n barco caido en ", "[", i, "]", "[", j, "]")

			} else {
				print("\nencontre 1 barco ")
				return false
			}
		}
	}

	return false
}
func atacar(mp [][]barco) {
	for i := 0; i < len(mp); i++ {
		for j := 0; j < len(mp); j++ {
			if mp[i][j].numero != 0 && mp[i][j].horizontal == true && mp[i][j].ataque == true && mp[i][j].vida != 3 { //si encontramos barcos entonces verificar posiciones siguientes y es horizontal
				aux := mp[i][j].numero //guardo para saber el id del barco para que reconozca los otros del mismo numero
				mp[i][j+1].ataque = false
				mp[i][j+2].ataque = false
				x := rand.Intn(len(mp))
				y := rand.Intn(len(mp))

				if mp[x][y].numero == aux { //posicion del mismo barco vuelve a randomearW
					for {
						s1 := rand.Intn(len(mp) - 1)
						s2 := rand.Intn(len(mp) - 1)
						if mp[x][y].numero == aux {
							x = s1
							y = s2
							break
						}
					}
					if mp[x][y].numero != 0 && mp[x][y].vida == 0 { // si hay un barco
						print("\n barco Numero ", aux, " ataco : ", "[", x, "]", "[", y, "] acerto \n ")
						mp[x][y].vida = 3
					} else if mp[x][y].numero != 0 && mp[x][y].vida == 3 {
						print("ya ataque aqui")
					} else {
						print("\n barco Numero ", aux, " ataco : ", "[", x, "]", "[", y, "] fallo\n ")
					}
				} else { // ataca cualquier parte del mapa
					print(" barco N ", aux, " ataco en =  [", x, "]", "[", y, "] fallo \n ")
				}
			} else {
			}
			print("")
		}
	}
}

func crear_barco(cant_jugadores int, cant_barcos int) []barco {

	var vector_barco []barco //creamos la variable para guardar los datos barco

	for i := 0; i < cant_barcos; i++ {
		vector_barco = append(vector_barco, inicializar_barco()) // agregar los datos
		vector_barco[i].numero = vector_barco[i].numero + i
		vector_barco[i].ataque = true
	}
	return vector_barco
}

func imprimir(mp [][]barco) {
	print(" º")
	for k := 0; k < len(mp); k++ {
		print("  ", k, "")
	}
	for i := 0; i < len(mp); i++ {
		print("\n ", i, " ")
		for j := 0; j < len(mp); j++ {
			var aux, aux2 barco
			aux.id = 1
			aux = mp[i][j]
			if aux.id == aux2.id {
				print(" - ")
			} else {
				if mp[i][j].vida == 3 {
					print(" ", "x", " ")
				} else {
					print(" ", aux.numero, " ")
				}
			}
		}
	}
}

func main() {

	cant_jugadores, _ := strconv.Atoi(os.Args[1])
	cant_barcos, _ := strconv.Atoi(os.Args[2])
	x, _ := strconv.Atoi(os.Args[3])
	y, _ := strconv.Atoi(os.Args[4])

	print("cantidad jugadores = ", cant_jugadores)
	print("\ncantidad barcos = ", cant_barcos)

	//crear mapa*
	mp := make([][]barco, x)
	for i := 0; i < x; i++ {
		mp[i] = make([]barco, y)
	}

	var vector []barco
	vector = crear_barco(cant_jugadores, cant_barcos)
	insert_barcos_matriz(vector, mp, 0)
	print("\n")
	imprimir(mp)
	print("\n")
	for {
		atacar(mp)
		print("\n")
		imprimir(mp)
		print("\n")
		if 0 == 1 {
			break
		}
	}
}
