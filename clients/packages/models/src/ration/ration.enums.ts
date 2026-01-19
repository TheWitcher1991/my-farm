import { EnumType } from '@farm/types'

export const BatchUnit = {
	KG: 'kg',
	L: 'l',
	PCS: 'pcs',
	PKG: 'pkg',
} as const

export type BatchUnit = EnumType<typeof BatchUnit>
