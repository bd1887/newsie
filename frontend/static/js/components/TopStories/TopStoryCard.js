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

class TopStoryCard extends Component {
  constructor(props) {
    super(props)
  }

  render() {
      let imgUrl = `url(${this.props.img})`
      let boxClass = this.getBoxClass();
      let titleSize = this.getTitleSize();
      let descriptionSize = this.getDescriptionSize();
      let className = `${categories[this.props.category]} ${boxClass}`
      return(
        <Box
            onClick={() => this.props.clickHandler(this.props.id)}
            className={className}
            elevation="xlarge"
            round="small"
            height="medium"
            background = {imgUrl}
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
                    className="headline card-text"
                    gridArea="titleArea"
                    size={titleSize}
                >{this.props.title}</Text>
                <Text
                    className="description card-text"
                    gridArea="descriptionArea"
                    size={descriptionSize}
                    alignSelf="start"
                >{this.props.description}</Text>

            </Grid>
        
        </Box>
      )
  }

  getBoxClass() {
    if (this.props.size >= 20) {
        return "top-story-box lg-box"
    } else if (this.props.size >= 5) {
        return "top-story-box md-box"
    } else {
        return "top-story-box sm-box"
    }
  }
  getTitleSize() {
    if (this.props.size >= 4) {
        return "xlarge"
    } else {
        return "large"
    }
  }
  getDescriptionSize() {
    if (this.props.size >= 4) {
        return "large"
    } else {
        return "medium"
    }
  }

}

export default TopStoryCard
