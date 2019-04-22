import React from 'react'
import { Switch, Route } from 'react-router-dom'
import RedirectToTopStores from './RedirectToTopStories'
import TopStories from './TopStories/TopStories'
import ExclusiveStories from './ExclusiveStories/ExclusiveStories'


const Main = () => (
  <main>
    <Switch>
      <Route exact path='/' component={RedirectToTopStores}/>
      <Route path='/top-stories' component={TopStories}/>
      <Route path='/exclusive-stories' component={ExclusiveStories}/>
    </Switch>
  </main>
)

export default Main
