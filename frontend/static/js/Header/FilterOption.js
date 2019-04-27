import React, { Component } from 'react';
import { Box, Text } from 'grommet';
import './FilterOption.css';

class FilterOption extends Component {

    constructor(props) {
        super(props)
      }


  
  render() {
    return (
        <Box
            className={this.props.className}
            align="center"
            onClick={() => {this.props.clickHandler(this.props.category)}}
        >
        <Text
        className="menu-item-text"
        size="medium"
        weight="bold"
        >
            {this.props.category}
        </Text>
            
        </Box>
    );
  }
}

export default FilterOption