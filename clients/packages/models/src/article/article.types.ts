import z from 'zod'

import { InjectProps, PaginateQuery } from '@farm/types'

import {
	articleId,
	ReadonlyArticleModel,
	WritableArticleModel,
} from './article.model'

export type ArticleID = z.infer<typeof articleId>

export type IArticle = z.infer<typeof ReadonlyArticleModel>

export type ICreateArticle = z.infer<typeof WritableArticleModel>

export type IUpdateArticle = z.infer<typeof WritableArticleModel>

export type WithArticleID = InjectProps<'article', ArticleID>

export type WithArticle = InjectProps<'article', IArticle>

export type UseArticles = PaginateQuery
