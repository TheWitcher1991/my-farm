import { object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

export const feedId = brand(shapes.id, 'FeedID')

export const BaseFeedModel = object({
	title: shapes.title,
	description: shapes.description,
})

export const ReadonlyFeedModel = BaseModel.extend({
	id: feedId,
	image: shapes.url,
	...BaseFeedModel.shape,
})

export const WritableFeedModel = BaseFeedModel.extend({
	image: shapes.image,
})
