import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { articleConfig } from './ration.config'
import {
	ArticleID,
	IArticle,
	ICreateArticle,
	IUpdateArticle,
	UseArticles,
} from './ration.types'

export const createReadonlyArticleApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<
		Paginated<IArticle>,
		IArticle,
		UseArticles,
		ArticleID
	>(http, {
		list: articleConfig.models,
		detail: articleConfig.model,
		infinity: articleConfig.infinityModels,
	})

	return {
		useArticles: api.useEntities,
		useArticle: api.useEntity,
		useInfinityArticles: api.useInfinityEntities,
		articleRepository: api.repo,
	}
}

export const createArticleApi = (http: HttpClientInstance) => {
	const api = createApi<
		Paginated<IArticle>,
		IArticle,
		ICreateArticle,
		IUpdateArticle,
		UseArticles,
		ArticleID
	>(http, {
		list: articleConfig.models,
		detail: articleConfig.model,
		infinity: articleConfig.infinityModels,
	})

	return {
		useArticles: api.useEntities,
		useArticle: api.useEntity,
		useInfinityArticles: api.useInfinityEntities,
		useCreateArticle: api.useCreateEntity,
		useAddArticle: api.useAddEntity,
		useUpdateArticle: api.useUpdateEntity,
		useEditArticle: api.useEditEntity,
		useDeleteArticle: api.useDeleteEntity,
		articleRepository: api.repo,
	}
}
