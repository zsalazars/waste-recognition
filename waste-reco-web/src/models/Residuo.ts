export interface Residuo {
  id: number
  nombre: string
  categoria: number
}

export interface ResiduoCategoria {
  id: number
  nombre: string
  residuos: Residuo[]
}
