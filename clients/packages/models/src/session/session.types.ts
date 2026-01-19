import z from 'zod'

import { InjectProps } from '@farm/types'

import { SessionModel } from './session.model'

export type ISession = z.infer<typeof SessionModel>

export type WithSession = InjectProps<'session', ISession>
