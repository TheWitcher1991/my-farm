import { ArticleID } from './ration.types'

export const toArticleID = (id: number | string): ArticleID =>
	Number(id) as ArticleID
