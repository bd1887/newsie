import React, { Component } from 'react';
import { Box, Grid, Image, Text } from 'grommet';
import './SmallStoryCard.css';

const categories = {
  'Sports': 'sports-story',
  'Business and Finance': 'business-and-finance-story',
  'Ireland': 'ireland-story',
  'Entertainment': 'entertainment-story',
  'Health': 'health-story',
  'Education': 'education-story',
  'World': 'world-story'
}

class SmallStoryCard extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    let className = `small-story-box ${categories[this.props.category]}`
    console.log(className)
    return (
      <Box 
        onClick={() => this.props.clickHandler(this.props.id)}
        className={className}
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

export default SmallStoryCard