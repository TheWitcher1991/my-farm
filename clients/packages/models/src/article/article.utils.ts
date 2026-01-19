import { ArticleID } from './article.types'

export const toArticleID = (id: number | string): ArticleID =>
	Number(id) as ArticleID
