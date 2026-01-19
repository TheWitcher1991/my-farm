import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { feedConfig } from './feed.config'
import { FeedID, ICreateFeed, IFeed, IUpdateFeed, UseFeeds } from './feed.types'

export const createReadonlyFeedApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<Paginated<IFeed>, IFeed, UseFeeds, FeedID>(
		http,
		{
			list: feedConfig.models,
			detail: feedConfig.model,
			infinity: feedConfig.infinityModels,
		},
	)

	return {
		useFeeds: api.useEntities,
		useFeed: api.useEntity,
		useInfinityFeeds: api.useInfinityEntities,
		feedRepository: api.repo,
	}
}

export const createFeedApi = (http: HttpClientInstance) => {
	const api = createApi<
		Paginated<IFeed>,
		IFeed,
		ICreateFeed,
		IUpdateFeed,
		UseFeeds,
		FeedID
	>(http, {
		list: feedConfig.models,
		detail: feedConfig.model,
		infinity: feedConfig.infinityModels,
	})

	return {
		useFeeds: api.useEntities,
		useFeed: api.useEntity,
		useInfinityFeeds: api.useInfinityEntities,
		useCreateFeed: api.useCreateEntity,
		useAddFeed: api.useAddEntity,
		useUpdateFeed: api.useUpdateEntity,
		useEditFeed: api.useEditEntity,
		useDeleteFeed: api.useDeleteEntity,
		feedRepository: api.repo,
	}
}
