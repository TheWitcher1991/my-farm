import { createApi, createReadonlyApi, HttpClientInstance } from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { weightConfig } from './weight.config'
import {
	ICreateWeight,
	IUpdateWeight,
	IWeight,
	UseWeights,
	WeightID,
} from './weight.types'

export const createReadonlyFeedApi = (http: HttpClientInstance) => {
	const api = createReadonlyApi<
		Paginated<IWeight>,
		IWeight,
		UseWeights,
		WeightID
	>(http, {
		list: weightConfig.models,
		detail: weightConfig.model,
		infinity: weightConfig.infinityModels,
	})

	return {
		useWeights: api.useEntities,
		useWeight: api.useEntity,
		useInfinityWeights: api.useInfinityEntities,
		weightRepository: api.repo,
	}
}

export const createFeedApi = (http: HttpClientInstance) => {
	const api = createApi<
		Paginated<IWeight>,
		IWeight,
		ICreateWeight,
		IUpdateWeight,
		UseWeights,
		WeightID
	>(http, {
		list: weightConfig.models,
		detail: weightConfig.model,
		infinity: weightConfig.infinityModels,
	})

	return {
		useWeights: api.useEntities,
		useWeight: api.useEntity,
		useInfinityWeights: api.useInfinityEntities,
		useCreateWeight: api.useCreateEntity,
		useAddWeight: api.useAddEntity,
		useUpdateWeight: api.useUpdateEntity,
		useEditWeight: api.useEditEntity,
		useDeleteWeight: api.useDeleteEntity,
		weightRepository: api.repo,
	}
}
