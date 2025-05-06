export interface WastePayload {
  categoria: string
  cantidad: number
}

export interface EmailPayload {
  subject: string
  body: string
  to: string
  start_date: string
  end_date: string
  depositos: WastePayload[]
}
