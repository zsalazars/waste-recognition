import type { Residuo } from './Residuo'
import type { Usuario } from './Usuario'

export default interface Reporte {
  id: number
  precision_usuario: number
  tasa_acierto: number
  fecha_prediccion: string
  tacho_esperado: boolean
  id_residuo: number
  id_usuario: number
}

export interface ReporteResponse {
  id: number
  precision_usuario: number
  tasa_acierto: number
  fecha_prediccion: string
  tacho_esperado: boolean
  residuo: Residuo
  usuario: Usuario
}

export const defaultReporte: Reporte = {
  id: 0,
  precision_usuario: 0,
  tasa_acierto: 0,
  fecha_prediccion: '',
  tacho_esperado: false,
  id_residuo: 0,
  id_usuario: 0,
}
