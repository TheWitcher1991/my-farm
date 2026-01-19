import { nativeEnum, object } from 'zod'

import { brand, shapes } from '@farm/toolkit'

import { UserRole } from './user.enums'

export const userId = brand(shapes.id, 'UserID')

export const BaseUserModel = object({
	email: shapes.email,
	phone: shapes.phone,
	first_name: shapes.title,
	last_name: shapes.description,
	surname: shapes.title.optional(),
	role: nativeEnum(UserRole),
})

export const ReadonlyUserModel = object({
	id: userId,
	date_joined: shapes.datetime,
	updated_at: shapes.datetime,
})

export const WritableUserModel = BaseUserModel.extend({})
