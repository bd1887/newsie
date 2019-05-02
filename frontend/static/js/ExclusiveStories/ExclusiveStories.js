import React, { Component } from 'react';
import axios from 'axios';
import { Box, InfiniteScroll, Text } from 'grommet';
import { Gremlin } from 'grommet-icons';
import './ExclusiveStories.css';

import SmallCard from '../Shared/SmallCard';
import ArticleModal from '../Shared/ArticleModal';
import { Link } from 'react-router-dom';


class ExclusiveStories extends Component {

  constructor(props) {
    super(props)
    this.state = {
      storyList: [],
      loading: true,
      showModal: false,
      selectedStory: null,
      offset: 0,
      fetchingData: false
    }
    this.filters = this.props.filters
    this.getData = this.getData.bind(this)
    this.getMoreData = this.getMoreData.bind(this)
    this.setShow = this.setShow.bind(this)
    this.onStoryCardClick = this.onStoryCardClick.bind(this)
  }

  componentWillMount () {
    this.getData(this.props.filters);
  }

  componentWillReceiveProps(newProps) {
    if (!this.arraysEqual(newProps.filters, this.filters)) {
      this.setState({storyList: [], loading: true})
      this.offset = 0;
      this.getData(newProps.filters)
    }
  }

  setShow(bool) {
    this.setState({showModal: bool})
  }

  onStoryCardClick(id) {
    let story = this.state.storyList.filter(story => {
      return story.id === id
    })
    console.log(story)
    this.setState({ selectedStory: story[0], showModal: true })
  }

  getData(filters) {
    if (!this.state.fetchingData) {
      let filters_query = filters && filters.length ? '&categories=' + filters.join(',') : ''
      let query = '/api/exclusive-stories/?limit=20&offset=0' + filters_query
      console.log(query)
      axios.get(query)
      .then(response => {
        this.setState({   
          storyList: response.data.results,
          loading: false,
          offset: 20
        })
        this.filters = []
        this.filters = this.filters.concat(filters)
      })
    }
  }

  getMoreData() {
    if (!this.state.fetchingData) {
      let filters = this.props.filters
      let filters_query = filters && filters.length ? '&categories=' + filters.join(',') : ''
      let query = '/api/exclusive-stories/?limit=20&offset=' + this.state.offset + filters_query
      axios.get(query)
      .then(response => {
        this.setState({   
          storyList: this.state.storyList.slice().concat(response.data.results),
          fetchingData: false,
          offset: this.state.offset + 20
        })
      })
    }
    
  }

  arraysEqual(a,b) { return !!a && !!b && !(a<b || b<a); }

  render() {
    return (
      <Box className="infinite-scroll-box">
      {this.state.showModal && (
            <ArticleModal setShow={this.setShow} story={this.state.selectedStory}/>
          )}
        <InfiniteScroll
          items={this.state.storyList}
          step={10}
          replace={true}
          onMore={() => this.getMoreData()}>
          {(story) => (
                <SmallCard
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

export default ExclusiveStories

const ITEMS = [];
while (ITEMS.length < 100) ITEMS.push(ITEMS.length);