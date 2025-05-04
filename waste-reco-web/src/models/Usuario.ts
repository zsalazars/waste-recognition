export interface Usuario {
  id: number
  nombre: string
  email: string
}

export const defaultUser: Usuario = {
  id: 0,
  nombre: '',
  email: ''
}
