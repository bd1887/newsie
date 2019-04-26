import React from 'react'
import { Switch, Route } from 'react-router-dom'
import RedirectToTopStores from './Shared/RedirectToTopStories'
import TopStories from './TopStories/TopStories'
import ExclusiveStories from './ExclusiveStories/ExclusiveStories'


const Main = (props) => (
  
  <main>
    <Switch>
      <Route exact path='/' component={RedirectToTopStores}/>
      <Route
        path='/top-stories'
        render={(routeProps) => (
          <TopStories {...routeProps} filters={props.filters} />
        )}
      />
      <Route
        path='/exclusive-stories'
        render={(routeProps) => (
          <ExclusiveStories {...routeProps} filters={props.filters} />
        )}
      />
    </Switch>
  </main>
)

export default Main
