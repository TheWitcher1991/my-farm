import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'

import { categoryConfig } from './category.config'
import {
	CategoryID,
	ICategory,
	ICreateCategory,
	IUpdateCategory,
	UseCategories,
} from './category.types'

export const createReadonlyCategoryApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<
		ICategory[],
		ICategory,
		UseCategories,
		CategoryID
	>(http, {
		list: categoryConfig.models,
		detail: categoryConfig.model,
		infinity: categoryConfig.infinityModels,
	})

	return {
		useCategories: api.useEntities,
		useCategory: api.useEntity,
		useInfinityCategories: api.useInfinityEntities,
		categoryRepository: api.repo,
	}
}

export const createCategoryApi = (http: HttpClientInstance) => {
	const api = createApi<
		ICategory[],
		ICategory,
		ICreateCategory,
		IUpdateCategory,
		UseCategories,
		CategoryID
	>(http, {
		list: categoryConfig.models,
		detail: categoryConfig.model,
		infinity: categoryConfig.infinityModels,
	})

	return {
		useCategories: api.useEntities,
		useCategory: api.useEntity,
		useInfinityCategories: api.useInfinityEntities,
		useCreateCategory: api.useCreateEntity,
		useAddCategory: api.useAddEntity,
		useUpdateCategory: api.useUpdateEntity,
		useEditCategory: api.useEditEntity,
		useDeleteCategory: api.useDeleteEntity,
		categoryRepository: api.repo,
	}
}
