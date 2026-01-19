import z from 'zod'

import { InjectProps } from '@farm/types'

import {
	categoryId,
	ReadonlyCategoryModel,
	WritableCategoryModel,
} from './category.model'

export type CategoryID = z.infer<typeof categoryId>

export type ICategory = z.infer<typeof ReadonlyCategoryModel>

export type ICreateCategory = z.infer<typeof WritableCategoryModel>

export type IUpdateCategory = z.infer<typeof WritableCategoryModel>

export type WithCategoryID = InjectProps<'category', CategoryID>

export type WithCategory = InjectProps<'category', ICategory>

export type UseCategories = {}
