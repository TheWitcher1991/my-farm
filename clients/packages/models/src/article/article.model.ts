import { categoryId, ReadonlyCategoryModel } from '../category'
import { ReadonlyUserModel, userId } from '../user'
import { nativeEnum, object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

import { ArticleStatus } from './article.enums'

export const articleId = brand(shapes.id, 'ArticleID')

export const BaseArticleModel = object({
	title: shapes.title,
	content: shapes.description,
	status: nativeEnum(ArticleStatus),
})

export const ReadonlyArticleModel = BaseModel.extend({
	id: articleId,
	cover: shapes.url,
	category: ReadonlyCategoryModel,
	author: ReadonlyUserModel,
	...BaseArticleModel.shape,
})

export const WritableArticleModel = BaseArticleModel.extend({
	category: categoryId,
	author: userId,
	cover: shapes.image,
})
