import React, { Component } from 'react';
import axios from 'axios';
import { Box, InfiniteScroll, Text } from 'grommet';
import './ExclusiveStories.css';
import SmallStoryCard from '../SmallStoryCard/SmallStoryCard';
import ArticleModal from '../ArticleModal/ArticleModal';
import { Link } from 'react-router-dom';


class ExclusiveStories extends Component {

  constructor(props) {
    super(props)
    this.state = {
      storyList: [],
      loading: true,
      showModal: false,
      selectedStory: null
    }
    this.offset = 0;
    this.getData = this.getData.bind(this)
    this.setShow = this.setShow.bind(this)
    this.onStoryCardClick = this.onStoryCardClick.bind(this)
    this.getMoreData = this.getMoreData.bind(this)
  }

  componentWillMount () {
    this.getData();
  }

  setShow(bool) {
    this.setState({showModal: bool})
  }

  onStoryCardClick(id) {
    console.log(this.state.storyList)
    let story = this.state.storyList.filter(story => {
      return story.id === id
    })
    this.setState({ selectedStory: story[0], showModal: true })
  }

  getData() {
    axios.get('/api/exclusive-stories/?limit=10&offset=0')
    .then(response => {
      this.setState({   
        storyList: response.data.results,
        loading: false
      })
    })
  }

  getMoreData() {
    this.offset += 10;
    axios.get('/api/exclusive-stories/?limit=10&offset=' + this.offset)
    .then(response => {
      this.setState({
        storyList: this.state.storyList.slice().concat(response.data.results)
      });
      
    })
  }

  render() {
    if (this.state.loading) {
      return (<p>loading...</p>)
    } else {
      return (
        <Box className="infinite-scroll-box">

          {this.state.showModal && (
            <ArticleModal setShow={this.setShow} story={this.state.selectedStory}/>
          )}
          
          <InfiniteScroll items={this.state.storyList}
            step={7}
            onMore={this.getMoreData}
          >
            {(story) => (
              <SmallStoryCard
                key={story.id}
                id={story.id}
                title={story.articles[0].title}
                description={story.articles[0].description}
                img={story.articles[0].img}
                category={story.category}
                clickHandler = {this.onStoryCardClick}
              />
            )}
          </InfiniteScroll>
        </Box>
      )
      
    }

  }
}

export default ExclusiveStories