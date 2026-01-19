import { $session } from './session.atom'

export const useSessionRequestInterceptor = config => {
	const jwt = $session.getState()
	const token_type = $session.getState()
	config.headers.Authorization = `${token_type} ${jwt}`
	return config
}
