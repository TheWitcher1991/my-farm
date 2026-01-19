import { DocumentID } from './document.types'

export const toDocumentID = (id: number | string): DocumentID =>
	Number(id) as DocumentID
