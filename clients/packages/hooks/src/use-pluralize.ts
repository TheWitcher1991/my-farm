import { pluralize } from '@farm/toolkit'

import { useMemoizedFn } from './use-memoized-fn'

export const usePluralize = () => useMemoizedFn(pluralize)