import React, { Component } from 'react';
import { Box, Grid, Text } from 'grommet';
import './TopStoryCard.css'

const categories = {
    'Sports': 'sports-top-story',
    'Business and Finance': 'business-and-finance-top-story',
    'Ireland': 'ireland-top-story',
    'Entertainment': 'entertainment-top-story',
    'Health': 'health-top-story',
    'Education': 'education-top-story',
    'World': 'world-top-story'
  }
  
//   The max number of characters before text is truncated
const truncationValues = {
    'sm-box': 55,
    'md-box': 70,
    'lg-box': 120,
    'mobile-box': 80
}

class TopStoryCard extends Component {
  constructor(props) {
    super(props)
  }

  render() {
    let imgUrl = `url(${this.props.img})`
    let className = `${categories[this.props.category]} top-story-box ${this.props.boxSize}`
    let truncationValue = truncationValues[this.props.boxSize]

    return(
    <Box
        onClick={() => this.props.clickHandler(this.props.id)}
        className={className}
        elevation="xlarge"
        round="small"
        height="medium"
        background = {{
            "color": "dark-2",
            "opacity": "medium",
            "position": "bottom",
            "image": imgUrl
            }}
    >
        <Grid 
            fill={true}
            className="grid"
            rows={['1/3', '1/3', '1/3']}
            columns={['fill']}
            areas={[
                {name: 'titleArea', start: [0,0], end: [0,0]},
                {name: 'gutterArea', start: [0,1], end: [0,1]},
                {name: 'descriptionArea', start: [0,2], end: [0,2]}
            ]}
        >

            <Text
                className='headline card-text'
                gridArea="titleArea"
            >{this.truncateText(this.props.title, truncationValue)}</Text>
            <Text
                className='description card-text'
                gridArea="descriptionArea"
                alignSelf="end"
            >{this.truncateText(this.props.description, truncationValue)}</Text>

        </Grid>
    
    </Box>
    )
  }

  truncateText(str, maxLength) {
      if (str.length > maxLength) {
          let lastSpace = str.lastIndexOf(" ", maxLength)
          return str.substring(0, lastSpace) + '...'
      }
      return str;
  }

}

export default TopStoryCard
