import { ReadonlyUserModel, userId } from '../user'
import { object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

import { WeightField } from './weight.enums'

export const weightId = brand(shapes.id, 'WeightID')

export const BaseWeightModel = object({
	title: shapes.title,
	[WeightField.CHEST_GIRTH]: shapes.positive,
	[WeightField.BODY_LENGTH]: shapes.positive,
})

export const ReadonlyWeightModel = BaseModel.extend({
	id: weightId,
	[WeightField.RESULT_WEIGTH]: shapes.positive,
	user: ReadonlyUserModel,
	...BaseWeightModel.shape,
})

export const WritableWeightModel = BaseWeightModel.extend({
	user: userId,
})
