import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { documentConfig } from './document.config'
import {
	DocumentID,
	ICreateDocument,
	IDocument,
	IUpdateDocument,
	UseDocuments,
} from './document.types'

export const createReadonlyDocumentRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<
		Paginated<IDocument>,
		IDocument,
		UseDocuments,
		DocumentID
	>(http, documentConfig.models)

export const createDocumentRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		Paginated<IDocument>,
		IDocument,
		ICreateDocument,
		IUpdateDocument,
		UseDocuments,
		DocumentID
	>(http, documentConfig.models)
