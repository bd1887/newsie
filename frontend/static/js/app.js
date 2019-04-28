import React, { Component } from 'react';
import { Box, Grommet } from 'grommet'
import Header from './Header/Header';
import Main from './Main';

const theme = {
  global: {
    font: {
      family: 'Roboto',
      size: '14px',
      height: '20px',
    },
  },
};

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      filters: [],
      dateRange: 'Today'
    }
    this.updateFilters = this.updateFilters.bind(this)
    this.updateDateRange = this.updateDateRange.bind(this)
  }

  render() {

    return (
      <Grommet theme={theme}>
        {/* <Box> */}
          <Header
            updateFilters={this.updateFilters}
            updateDateRange={this.updateDateRange}
            filters={this.state.filters}
            dateRange={this.state.dateRange}
            />
          <Main filters={this.state.filters} dateRange={this.state.dateRange}/>
        {/* </Box> */}
      </Grommet>
    );
  }

  updateFilters(key) {
    let filterArray = this.state.filters
        if (filterArray.includes(key)) {
            let keyRemovedArray = filterArray.filter( el => el != key)
            return this.setState({filters: keyRemovedArray})
        } else {
          filterArray.push(key)
            return this.setState({filters: filterArray})
        }
  }

  updateDateRange(option) {
    this.setState({dateRange: option})
  }

}

export default App;
