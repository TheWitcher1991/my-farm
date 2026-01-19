import z from 'zod'

import { InjectProps } from '@farm/types'

import {
	ReadonlyWeightModel,
	weightId,
	WritableWeightModel,
} from './weight.model'

export type WeightID = z.infer<typeof weightId>

export type IWeight = z.infer<typeof ReadonlyWeightModel>

export type ICreateWeight = z.infer<typeof WritableWeightModel>

export type IUpdateWeight = z.infer<typeof WritableWeightModel>

export type WithWeightID = InjectProps<'weight', WeightID>

export type WithWeight = InjectProps<'weight', IWeight>

export type UseWeights = {}
