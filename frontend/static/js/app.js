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
  render() {
    return (
      <Grommet padding="small" theme={theme} >
        <Box>
          <Header />
          <Main />
        </Box>
      </Grommet>
    );
  }
}

export default App;
