import React, { Component } from 'react';
import { withRouter } from 'react-router-dom'
import { Article } from 'grommet-icons';
import { Box, Tab, Tabs, Text } from 'grommet';
import CategoryFilter from './CategoryFilter/CategoryFilter';
import './Header.css';

// The Header creates tabs that can be used to navigate
// between routes.
class Header extends Component {

  constructor(props) {
    super(props)
    this.tabOnActiveHandler = this.tabOnActiveHandler.bind(this)
  }

  
  render() {
    return (
      <Box className="header">
        <Text margin="none" size="large" weight="bold" style={{ cursor: 'default'}}>NEW<Article></Article>SIE</Text>
        <Tabs className="stories-tabs" onActive={(i) => this.tabOnActiveHandler(i)} alignSelf='center'>
          <Tab title='Top Stories'>
          </Tab>
          <Tab title='Exclusive Stories'>
          </Tab>
        </Tabs>
        <CategoryFilter />
      </Box>
    );
  }

  tabOnActiveHandler(i) {
    let routes = ['/top-stories', '/exclusive-stories']
    let routeString = routes[i]
    this.props.history.push(routeString)
  }

}

export default withRouter(Header)