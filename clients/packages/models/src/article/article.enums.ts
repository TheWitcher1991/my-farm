import { EnumType } from '@farm/types'

export const ArticleStatus = {
	DRAFT: 'draft',
	PUBLISHED: 'published',
} as const

export type ArticleStatus = EnumType<typeof ArticleStatus>
