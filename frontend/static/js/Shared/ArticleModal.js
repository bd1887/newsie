import React, { Component } from 'react';
import { Box, InfiniteScroll, Layer, Text } from 'grommet';
import { Close, Gremlin } from 'grommet-icons';
import SmallCard from './SmallCard';
import MediaQuery from "react-responsive";
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
    return(
      <MediaQuery maxWidth={950}>
        {(matches) => {
          if (matches) {
            return this.getMobileView();
          } else {
            return this.getDesktopView();
          }
        }}
      </MediaQuery>
    )
  }
  getMobileView() {
      return (
        <Layer
          full={true}
          onEsc={() => this.props.setShow(false)}
          onClickOutside={() => this.props.setShow(false)}
          >
          <Box 
            onClick={() => this.props.setShow(false)}
            className="close-modal-mobile">
            <Close color="light-1"/>
          </Box>
          <Box
            pad="medium"
            overflow="scroll"
          >
            <InfiniteScroll items={this.props.story.articles}
              step={7}
            >
              {(article) => (
                <SmallCard
                  key={article.id}
                  id={article.id}
                  title={article.title}
                  description={article.description}
                  img={article.img}
                  clickHandler={this.onStoryCardClick}
                />
              )}
            </InfiniteScroll>

            <Box align="center" alignSelf="center">
              <Text size="xlarge" color="light-4">The End.</Text>
              <Gremlin size="xlarge" color="light-3" />
              <Text size="large" color="light-4">There are no more articles about this topic.</Text>
            </Box>

          </Box>
        </Layer>
    );
  }

  getDesktopView() {
      return (
        <Layer
          rounded="small"
          onEsc={() => this.props.setShow(false)}
          onClickOutside={() => this.props.setShow(false)}
          >
          <Box 
            onClick={() => this.props.setShow(false)}
            className="close-modal">
            <Close color="light-1"/>
          </Box>
          <Box
            border="all"
            round="small" 
            pad="small"
            overflow="scroll"
            width="large"
            height="large"
          >
            <InfiniteScroll items={this.props.story.articles}
              step={7}
            >
              {(article) => (
                <SmallCard
                  key={article.id}
                  id={article.id}
                  title={article.title}
                  description={article.description}
                  img={article.img}
                  clickHandler={this.onStoryCardClick}
                />
              )}
            </InfiniteScroll>

            <Box align="center" alignSelf="center">
              <Text size="xlarge" color="light-4">The End.</Text>
              <Gremlin size="xlarge" color="light-3" />
              <Text size="large" color="light-4">There are no more articles about this topic.</Text>
            </Box>

          </Box>
        </Layer>
    );
  }
}

export default ArticleModal