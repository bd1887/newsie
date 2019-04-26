import React, { Component } from 'react';
import { Box, Grid, Image, Text } from 'grommet';
import './SmallCard.css';



class SmallCard extends Component {

  categories = {
    'Sports': 'sports-story',
    'Business and Finance': 'business-and-finance-story',
    'Ireland': 'ireland-story',
    'Entertainment': 'entertainment-story',
    'Health': 'health-story',
    'Education': 'education-story',
    'World': 'world-story'
  }

  constructor(props) {
    super(props)
  }

  render() {
    if (this.props.filters) {
      if (this.props.filters.length !== 0 && !this.props.filters.includes(this.props.category)) {return null}
    }
    
    let className = `small-card-box ${this.categories[this.props.category]}`
    return (
      <Box 
        onClick={() => this.props.clickHandler(this.props.id)}
        round="small" 
        height="small"
        border="all"
        elevation="large"
        flex={false}
        >
        <Grid
          
          justifyContent="start"
          fill={true}
          rows={['50%', '50%']}
          columns={['20%', '80%']}
          gap="none"
          areas={[
            { name: 'headlineArea', start: [1, 0], end: [1, 0] },
            { name: 'imgArea', start: [0, 0], end: [0, 0] },
            { name: 'descArea', start: [0, 1], end: [1, 1] },
          ]}
        >
          <Box pad="small" gridArea="headlineArea">
            <Text size="large">{this.props.title}</Text>
          </Box>
          <Box pad="none" gridArea="imgArea" background="light-5">
            <Image
              className="small-card-img"
              fit="contain"
              src={this.props.img}
            />
          </Box>
          <Box pad="small" gridArea="descArea" background="light-2">
            <Text size="medium">{this.props.description}</Text>
          </Box>
        </Grid>
      </Box>
    );
  }
}

export default SmallCard