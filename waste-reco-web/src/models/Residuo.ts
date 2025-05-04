import type TiposResiduo from './TiposResiduo'

export interface Residuo {
  id: number
  nombre: string
  tipo_residuo: TiposResiduo
}

export interface ResiduoCategoria {
  id: number
  nombre: string
  residuos: Residuo[]
}
