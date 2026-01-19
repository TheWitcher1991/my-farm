import { modelConfig } from '@farm//toolkit'

import { WeightField } from './weight.enums'

export const weightConfig = modelConfig('weights')

export const WeightFieldMapper: Record<WeightField, string> = {
	[WeightField.CHEST_GIRTH]: 'Обхват груди',
	[WeightField.BODY_LENGTH]: 'Косая длина туловища',
	[WeightField.RESULT_WEIGTH]: 'Живая масса',
}
