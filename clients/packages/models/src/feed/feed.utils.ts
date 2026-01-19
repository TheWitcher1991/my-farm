import { FeedID } from './feed.types'

export const toFeedID = (id: number | string): FeedID => Number(id) as FeedID
