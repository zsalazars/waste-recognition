import type { EmailPayload } from '@/models/EmailPayload'
import http from '@/utils/axios'
import { defineStore } from 'pinia'

export const useEmailStore = defineStore('emailStore', () => {
  const sendEmail = async (emailData: EmailPayload) => {
    try {
      const response = await http.post('/email/send', emailData)
      return response.data
    } catch (error) {
      console.error('Error sending email:', error)
      throw error
    }
  }

  return {
    sendEmail,
  }
})
