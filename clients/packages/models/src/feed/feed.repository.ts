import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { feedConfig } from './feed.config'
import { FeedID, ICreateFeed, IFeed, IUpdateFeed, UseFeeds } from './feed.types'

export const createReadonlyFeedRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<Paginated<IFeed>, IFeed, UseFeeds, FeedID>(
		http,
		feedConfig.models,
	)

export const creatFeedRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		Paginated<IFeed>,
		IFeed,
		ICreateFeed,
		IUpdateFeed,
		UseFeeds,
		FeedID
	>(http, feedConfig.models)
