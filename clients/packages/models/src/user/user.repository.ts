import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { userConfig } from './user.config'
import { ICreateUser, IUpdateUser, IUser, UserID, UseUsers } from './user.types'

export const createReadonlyUserRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<Paginated<IUser>, IUser, UseUsers, UserID>(
		http,
		userConfig.models,
	)

export const createUserRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		Paginated<IUser>,
		IUser,
		ICreateUser,
		IUpdateUser,
		UseUsers,
		UserID
	>(http, userConfig.models)
