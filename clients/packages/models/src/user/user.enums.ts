import { EnumType } from '@farm/types'

export const UserRole = {
	SUPERADMIN: 'superadmin',
	ADMIN: 'admin',
	USER: 'user',
} as const

export type UserRole = EnumType<typeof UserRole>
