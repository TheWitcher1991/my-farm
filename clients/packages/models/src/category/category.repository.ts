import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'

import { categoryConfig } from './category.config'
import {
	CategoryID,
	ICategory,
	ICreateCategory,
	IUpdateCategory,
	UseCategories,
} from './category.types'

export const createReadonlyCategoryRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<ICategory[], ICategory, UseCategories, CategoryID>(
		http,
		categoryConfig.models,
	)

export const createCategoryRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		ICategory[],
		ICategory,
		ICreateCategory,
		IUpdateCategory,
		UseCategories,
		CategoryID
	>(http, categoryConfig.models)
