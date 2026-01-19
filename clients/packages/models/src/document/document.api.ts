import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { documentConfig } from './document.config'
import {
	DocumentID,
	ICreateDocument,
	IDocument,
	IUpdateDocument,
	UseDocuments,
} from './document.types'

export const createReadonlyArticleApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<
		Paginated<IDocument>,
		IDocument,
		UseDocuments,
		DocumentID
	>(http, {
		list: documentConfig.models,
		detail: documentConfig.model,
		infinity: documentConfig.infinityModels,
	})

	return {
		useDocuments: api.useEntities,
		useDocument: api.useEntity,
		useInfinityDocuments: api.useInfinityEntities,
		documentRepository: api.repo,
	}
}

export const createArticleApi = (http: HttpClientInstance) => {
	const api = createApi<
		Paginated<IDocument>,
		IDocument,
		ICreateDocument,
		IUpdateDocument,
		UseDocuments,
		DocumentID
	>(http, {
		list: documentConfig.models,
		detail: documentConfig.model,
		infinity: documentConfig.infinityModels,
	})

	return {
		useDocuments: api.useEntities,
		useDocument: api.useEntity,
		useInfinityDocuments: api.useInfinityEntities,
		useCreateDocument: api.useCreateEntity,
		useAddDocument: api.useAddEntity,
		useUpdateDocument: api.useUpdateEntity,
		useEditDocument: api.useEditEntity,
		useDeleteDocument: api.useDeleteEntity,
		documentRepository: api.repo,
	}
}
