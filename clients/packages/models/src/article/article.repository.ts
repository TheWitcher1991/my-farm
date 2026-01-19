import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { articleConfig } from './article.config'
import {
	ArticleID,
	IArticle,
	ICreateArticle,
	IUpdateArticle,
	UseArticles,
} from './article.types'

export const createReadonlyArticleRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<
		Paginated<IArticle>,
		IArticle,
		UseArticles,
		ArticleID
	>(http, articleConfig.models)

export const createArticleRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		Paginated<IArticle>,
		IArticle,
		ICreateArticle,
		IUpdateArticle,
		UseArticles,
		ArticleID
	>(http, articleConfig.models)
