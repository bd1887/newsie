import React, { Component } from 'react';
import { Box, Grommet } from 'grommet'
import Header from './components/Header/Header';
import Main from './components/Main';

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
      filters: []
    }
    this.updateFilters = this.updateFilters.bind(this)
  }

  render() {
    return (
      <Grommet padding="small" theme={theme} >
        <Box>
          <Header
            updateFilters={this.updateFilters}
            filters={this.state.filters}
            />
          <Main filters={this.state.filters}/>
        </Box>
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

}

export default App;
