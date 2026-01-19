import { EnumType } from '@farm/types'

export const DocumentStatus = {
	DRAFT: 'draft',
	PUBLISHED: 'published',
} as const

export type DocumentStatus = EnumType<typeof DocumentStatus>

export const DocumentViewType = {
	STATIC: 'static',
	DYNAMIC: 'dynamic',
} as const

export type DocumentViewType = EnumType<typeof DocumentViewType>
