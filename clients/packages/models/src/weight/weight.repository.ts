import {
	CrudRepository,
	HttpClientInstance,
	ReadonlyRepository,
} from '@farm/toolkit'
import { Paginated } from '@farm/types'

import { weightConfig } from './weight.config'
import {
	ICreateWeight,
	IUpdateWeight,
	IWeight,
	UseWeights,
	WeightID,
} from './weight.types'

export const createReadonlyFeedRepository = (http: HttpClientInstance) =>
	new ReadonlyRepository<Paginated<IWeight>, IWeight, UseWeights, WeightID>(
		http,
		weightConfig.models,
	)

export const creatFeedRepository = (http: HttpClientInstance) =>
	new CrudRepository<
		Paginated<IWeight>,
		IWeight,
		ICreateWeight,
		IUpdateWeight,
		UseWeights,
		WeightID
	>(http, weightConfig.models)
