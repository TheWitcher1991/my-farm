import { feedId, ReadonlyFeedModel } from '../feed'
import { ReadonlyUserModel, userId } from '../user'
import { nativeEnum, object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

import { BatchUnit } from './ration.enums'

export const rationId = brand(shapes.id, 'RationID')

export const rationFeedId = brand(shapes.id, 'RationFeedID')

export const BaseRationModel = object({
	title: shapes.title,
})

export const BaseRationFeedModel = object({
	quantity: shapes.positive,
	unit: nativeEnum(BatchUnit),
})

export const ReadonlyRationFeedModel = BaseModel.extend({
	id: rationFeedId,
	feed: ReadonlyFeedModel,
	...BaseRationModel.shape,
})

export const WritableRationFeedModel = BaseRationModel.extend({
	ration: rationId,
	feed: feedId,
})

export const ReadonlyRationModel = BaseModel.extend({
	id: rationId,
	user: ReadonlyUserModel,
	...BaseRationFeedModel.shape,
})

export const WritableRationModel = BaseRationFeedModel.extend({
	user: userId,
})
