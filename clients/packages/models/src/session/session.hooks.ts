import { useUnit } from 'effector-react'

import { $session } from './session.atom'

export const useSession = () => useUnit($session)

export const useCheckAuth = (): boolean => Boolean(useSession())
