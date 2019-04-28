import React, { Component } from 'react';
import axios from 'axios';
import './TopStories.css'
import TopStoryCard from './TopStoryCard'
import ArticleModal from '../Shared/ArticleModal';
import Masonry from 'react-masonry-component';
import MediaQuery from "react-responsive";
import { Box, Text } from 'grommet';
import { Gremlin } from 'grommet-icons';
import { Link } from 'react-router-dom';

const masonryOptions = {
  transitionDuration: '.4s',
  stagger: '.03s',
  resize: false,
  personPosition: true,
  horizontalOrder: false,
  columnWidth: 1,
  gutter: 5,
};

class TopStories extends Component {

  constructor(props) {
    super(props)
    this.state = {
      storyList: [],
      loading: true,
      showModal: false,
      selectedStory: null,
      articleCount: 0,
      dateRange: 'Today'
    }
    this.getData = this.getData.bind(this)
    this.onStoryCardClick = this.onStoryCardClick.bind(this)
    this.setShow = this.setShow.bind(this)
  }

  componentWillMount () {
    this.getData('Today');
  }

  componentWillReceiveProps(newProps) {
    if (newProps.dateRange !== this.state.dateRange) {
      this.getData(newProps.dateRange)
      this.setState({dateRange: newProps.dateRange})
    }
  }

  setShow(bool) {
    this.setState({showModal: bool})
  }

  onStoryCardClick(id) {
    let story = this.state.storyList.filter(story => {
      return story.id === id
    })
    this.setState({ selectedStory: story[0], showModal: true })
  }

  getData(dateRange) {
    dateRange = dateRange.toLowerCase().replace(' ', '_')
    axios.get('/api/top-stories/?date_range=' + dateRange)
    .then(response => {
      let articleCount = this.getArticleCount(response.data)
      this.setState({   
        storyList: response.data,
        loading: false,
        articleCount: articleCount
      })
    })
  }

  getArticleCount(storyList) {
    let sum = 0;
    storyList.forEach(story => {
      sum += story.articles.length
    });
    return sum
  }

  render() {
    if (this.state.loading) {
      return(
        <Box pad="large" align="center" alignSelf="center" flex={true}>
          <Text size="large" color="light-4">LOADING...</Text>
          <Gremlin size="large" color="light-3" />
        </Box>
      )
      
    } else {
      
      return(
        <Box className="top-stories-container">
        {this.state.showModal && (
            <ArticleModal setShow={this.setShow} story={this.state.selectedStory}/>
          )}
          <MediaQuery maxWidth={950}>
            {(matches) => {
              if (matches) {
                return (
                    this.getMobileView()
                )
              } else {
                return this.getMasonry();
              }
            }}
          </MediaQuery>
        </Box>
        
      )
    }
  }

  getMasonry() {
    let count = 0
      const storyCards = this.state.storyList.map(story => {
        let storyListLength = this.state.storyList.length
        let boxSize = count == 0 ? 'lg-box' : storyListLength - count > storyListLength / 2 ? 'md-box' : 'sm-box'
        count++

        if  (this.props.filters.length == 0 || this.props.filters.includes(story.category))
        return <TopStoryCard
            key={story.id}
            id={story.id}
            title={story.articles[0].title}
            description={story.articles[0].description}
            category={story.category}
            img={story.articles[0].img}
            size={story.size_this_week}
            clickHandler = {this.onStoryCardClick}
            boxSize = {boxSize}
          />
      })
      let storyCardsAreEmpty = this.areStoryCardsEmpty(storyCards)
      if (storyCardsAreEmpty) {
        return this.noResultsFound()
      }
      return (
          <Masonry
                className="masonry"
                options={masonryOptions}
                enableResizableChildren={true}
            >
                {storyCards}
          </Masonry>
      )
  }

  getMobileView() {
      let storyCards = this.state.storyList.map(story => {
          let boxSize = 'mobile-box'
  
          if  (this.props.filters.length == 0 || this.props.filters.includes(story.category))
          return <TopStoryCard
              key={story.id}
              id={story.id}
              title={story.articles[0].title}
              description={story.articles[0].description}
              category={story.category}
              img={story.articles[0].img}
              size={story.size_this_week}
              clickHandler = {this.onStoryCardClick}
              boxSize = {boxSize}
            />
        })

      let storyCardsAreEmpty = this.areStoryCardsEmpty(storyCards)
      if (storyCardsAreEmpty) {
        return this.noResultsFound()
      }
      return storyCards


  }

  areStoryCardsEmpty(arr) {
    let definedElement = arr.find((el) => {
      return el !== undefined
    })
    if (definedElement) {
      return false;
    }
    return true;
  }

  noResultsFound() {
    return (
      <Box align="center" alignSelf="center" style={{maxWidth: "100vw"}}>
        <Text size="xxlarge" color="light-4">No results found.</Text>
        <Gremlin size="xxlarge" color="light-3" />
        <Text size="xxlarge" color="light-4" alignSelf="center">Try adjusting the filters.</Text>
      </Box>
    )
  }

}

export default TopStories