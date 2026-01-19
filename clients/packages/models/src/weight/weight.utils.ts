import { WeightID } from './weight.types'

export const toWeightID = (id: number | string): WeightID =>
	Number(id) as WeightID
