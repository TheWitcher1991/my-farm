import { EnumType } from '@farm/types'

export const WeightField = {
	CHEST_GIRTH: 'chest_girth',
	BODY_LENGTH: 'body_length',
	RESULT_WEIGTH: 'result_weight',
} as const

export type WeightField = EnumType<typeof WeightField>
