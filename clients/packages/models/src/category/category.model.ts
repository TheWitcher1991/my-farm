import { object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

export const categoryId = brand(shapes.id, 'CategoryID')

export const BaseCategoryModel = object({
	title: shapes.title,
	description: shapes.description,
})

export const ReadonlyCategoryModel = BaseModel.extend({
	id: categoryId,
	...BaseCategoryModel.shape,
})

export const WritableCategoryModel = BaseCategoryModel.extend({})
