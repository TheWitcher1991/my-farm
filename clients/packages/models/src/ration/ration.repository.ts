import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { articleConfig } from './ration.config'
import {
	ArticleID,
	IArticle,
	ICreateArticle,
	IUpdateArticle,
	UseArticles,
} from './ration.types'

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
