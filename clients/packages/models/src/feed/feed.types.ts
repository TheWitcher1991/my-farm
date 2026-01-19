import z from 'zod'

import { InjectProps } from '@farm/types'

import { feedId, ReadonlyFeedModel, WritableFeedModel } from './feed.model'

export type FeedID = z.infer<typeof feedId>

export type IFeed = z.infer<typeof ReadonlyFeedModel>

export type ICreateFeed = z.infer<typeof WritableFeedModel>

export type IUpdateFeed = z.infer<typeof WritableFeedModel>

export type WithFeedID = InjectProps<'feed', FeedID>

export type WithFeed = InjectProps<'feed', IFeed>

export type UseFeeds = {}
