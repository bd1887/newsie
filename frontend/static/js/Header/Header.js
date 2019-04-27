import React, { Component } from 'react';
import { withRouter } from 'react-router-dom'
import { Article, Calendar, Close } from 'grommet-icons';
import { Box, Select, Tab, Tabs, Text } from 'grommet';
import CategoryFilter from './CategoryFilter';
import './Header.css';

// The Header creates tabs that can be used to navigate
// between routes.

const dateRangeOptions = ['Today', 'This Week', 'This Month', "All Time"]

class Header extends Component {

  constructor(props) {
    super(props)
    this.tabOnActiveHandler = this.tabOnActiveHandler.bind(this)
  }

  
  render() {
    return (
      <Box flex={true} className="header">
        <Text className="brand" margin="none" size="large" weight="bold" style={{ cursor: 'default'}}>NEW<Article></Article>SIE</Text>
        <Tabs className="stories-tab" onActive={(i) => this.tabOnActiveHandler(i)} alignSelf='center'>
          <Tab title='Top Stories'>
          </Tab>
          <Tab title='Exclusive Stories'>
          </Tab>
        </Tabs>
        <CategoryFilter filters={this.props.filters} updateFilters={this.props.updateFilters}/>

        <div className="date-container">
          <Select
            margin="xsmall"
            size="small"
            options={dateRangeOptions}
            value= {<Text className="date-range-text"><Calendar className="calendar"/>{this.props.dateRange}</Text>}
            onChange={({ option }) => this.props.updateDateRange(option)}
          />
        </div>  

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