import z from 'zod'

import { InjectProps, PaginateQuery } from '@farm/types'

import {
	documentId,
	ReadonlyDocumentModel,
	WritableDocumentModel,
} from './document.model'

export type DocumentID = z.infer<typeof documentId>

export type IDocument = z.infer<typeof ReadonlyDocumentModel>

export type ICreateDocument = z.infer<typeof WritableDocumentModel>

export type IUpdateDocument = z.infer<typeof WritableDocumentModel>

export type WithDocumentID = InjectProps<'document', DocumentID>

export type WithDocument = InjectProps<'document', IDocument>

export type UseDocuments = PaginateQuery
