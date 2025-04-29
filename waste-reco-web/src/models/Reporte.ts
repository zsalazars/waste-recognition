import type { Residuo } from './Residuo'
import type Usuario from './Usuario'

export default interface Reporte {
  id: number
  precision_usuario: number
  tasa_acierto: number
  fecha_reporte: string
  id_residuo: number
  id_usuario: number
}

export interface ReporteResponse {
  id: number
  precision_usuario: number
  tasa_acierto: number
  fecha_reporte: string
  residuo: Residuo
  usuario: Usuario
}
