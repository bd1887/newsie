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
    let className = `small-card-box ${this.categories[this.props.category]}`
    return (
      <Box 
        onClick={() => this.props.clickHandler(this.props.id)}
        className= {className}
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
          columns={['40%', '60%']}
          gap="none"
          areas={[
            { name: 'headlineArea', start: [1, 0], end: [1, 0] },
            { name: 'imgArea', start: [0, 0], end: [0, 1] },
            { name: 'descArea', start: [1, 1], end: [1, 1] },
          ]}
        >
          <Box pad="small" gridArea="headlineArea" round="small" >
            <Text size="large">{this.props.title}</Text>
          </Box>
          <Box className="small-card-img-box" pad="none" gridArea="imgArea" background="black" round="small" >
            <Image
              className="small-card-img"
              fit="contain"
              src={this.props.img}
            />
          </Box>
          <Box pad="small" gridArea="descArea" background="light-2" round="small">
            <Text size="medium">{this.props.description}</Text>
          </Box>
        </Grid>
      </Box>
    );
  }
}

export default SmallCard