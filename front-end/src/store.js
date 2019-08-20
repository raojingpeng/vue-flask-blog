/* eslint-disable no-console */
export default {
  debug: true,
  state: {
    is_new: false,
    is_authenticated: window.localStorage.getItem('ackerman-token') ? true : false,
    user_id: window.localStorage.getItem('ackerman-token') ? JSON.parse(atob(window.localStorage.getItem('ackerman-token').split('.')[1])).user_id : 0
  },
  setNewAction () {
    if (this.debug) { console.log('setNewAction triggered') }
    this.state.is_new = true
  },
  resetNotNewAction () {
    if (this.debug) { console.log('resetNotNewAction triggered') }
    this.state.is_new = false
  },
  loginAction () {
    if (this.debug) { console.log('loginAction triggered') }
    this.state.is_authenticated = true
    this.state.user_id = JSON.parse(atob(window.localStorage.getItem('ackerman-token').split('.')[1])).user_id
  },
  logoutAction () {
    if (this.debug) { console.log('logout triggered') }
    window.localStorage.removeItem('ackerman-token')
    this.state.is_authenticated = false
    this.state.user_id = 0
  }
}