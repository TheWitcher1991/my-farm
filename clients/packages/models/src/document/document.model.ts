import { ReadonlyUserModel, userId } from '../user'
import { nativeEnum, object } from 'zod'

import { BaseModel, brand, shapes } from '@farm/toolkit'

import { DocumentStatus, DocumentViewType } from './document.enums'

export const documentId = brand(shapes.id, 'DocumentID')

export const BaseDocumentModel = object({
	title: shapes.title,
	description: shapes.description,
	status: nativeEnum(DocumentStatus),
	view_type: nativeEnum(DocumentViewType),
})

export const ReadonlyDocumentModel = BaseModel.extend({
	id: documentId,
	file: shapes.url,
	author: ReadonlyUserModel,
	...BaseDocumentModel.shape,
})

export const WritableDocumentModel = BaseDocumentModel.extend({
	author: userId,
	file: shapes.document,
})
