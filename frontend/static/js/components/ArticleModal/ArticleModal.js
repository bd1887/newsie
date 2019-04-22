import React, { Component } from 'react';
import { Box, InfiniteScroll, Layer } from 'grommet';
import SmallStoryCard from '../SmallStoryCard/SmallStoryCard';
import './ArticleModal.css';


class ArticleModal extends Component {

  constructor(props) {
    super(props)
    this.onStoryCardClick = this.onStoryCardClick.bind(this)
  }

  onStoryCardClick(id) {
    let article = this.props.story.articles.filter(article => {
      return article.id === id
    })
    window.open(article[0].url, "_blank")
  }

  render() {
    return (
        <Layer
          onEsc={() => this.props.setShow(false)}
          onClickOutside={() => this.props.setShow(false)}
          >
          <Box
            border="all"
            round="medium" 
            pad="small"
            overflow="scroll"
            width="large"
            height="large"
          >
            <InfiniteScroll items={this.props.story.articles}
              step={7}
            >
              {(article) => (
                <SmallStoryCard
                  key={article.id}
                  id={article.id}
                  title={article.title}
                  description={article.description}
                  img={article.img}
                  clickHandler={this.onStoryCardClick}
                />
              )}
            </InfiniteScroll>
          </Box>
        </Layer>
    );
  }
}

export default ArticleModal