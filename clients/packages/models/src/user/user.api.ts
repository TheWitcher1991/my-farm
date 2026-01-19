import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { userConfig } from './user.config'
import { ICreateUser, IUpdateUser, IUser, UserID, UseUsers } from './user.types'

export const createReadonlyUserApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<Paginated<IUser>, IUser, UseUsers, UserID>(
		http,
		{
			list: userConfig.models,
			detail: userConfig.model,
			infinity: userConfig.infinityModels,
		},
	)

	return {
		useUsers: api.useEntities,
		useUser: api.useEntity,
		useInfinityUsers: api.useInfinityEntities,
		userRepository: api.repo,
	}
}

export const createUserApi = (http: HttpClientInstance) => {
	const api = createApi<
		Paginated<IUser>,
		IUser,
		ICreateUser,
		IUpdateUser,
		UseUsers,
		UserID
	>(http, {
		list: userConfig.models,
		detail: userConfig.model,
		infinity: userConfig.infinityModels,
	})

	return {
		useUsers: api.useEntities,
		useUser: api.useEntity,
		useInfinityUsers: api.useInfinityEntities,
		useCreateUser: api.useCreateEntity,
		useAddUser: api.useAddEntity,
		useUpdateUser: api.useUpdateEntity,
		useEditUser: api.useEditEntity,
		useDeleteUser: api.useDeleteEntity,
		userRepository: api.repo,
	}
}
