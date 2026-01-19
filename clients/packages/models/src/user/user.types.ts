import z from 'zod'

import { InjectProps, PaginateQuery } from '@farm/types'

import { ReadonlyUserModel, userId, WritableUserModel } from './user.model'

export type UserID = z.infer<typeof userId>

export type IUser = z.infer<typeof ReadonlyUserModel>

export type ICreateUser = z.infer<typeof WritableUserModel>

export type IUpdateUser = z.infer<typeof WritableUserModel>

export type WithUserID = InjectProps<'user', UserID>

export type WithUser = InjectProps<'user', IUser>

export type UseUsers = PaginateQuery
