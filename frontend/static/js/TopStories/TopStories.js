import React, { Component } from 'react';
import axios from 'axios';
import './TopStories.css'
import TopStoryCard from './TopStoryCard'
import ArticleModal from '../Shared/ArticleModal';
import Masonry from 'react-masonry-component';
import MediaQuery from "react-responsive";
import { Link } from 'react-router-dom';

const masonryOptions = {
  transitionDuration: 0,
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
      articleCount: 0
    }
    this.getData = this.getData.bind(this)
    this.onStoryCardClick = this.onStoryCardClick.bind(this)
    this.setShow = this.setShow.bind(this)
  }

  componentWillMount () {
    this.getData();
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

  getData() {
    axios.get('/api/top-stories/?date_range=this_month')
    .then(response => {
      console.log(response.data)
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
      return (<p>loading...</p>)
    } else {
      
      return(
        <MediaQuery maxWidth={950}>
          {(matches) => {
            if (matches) {
              return this.getMobileView();
            } else {
              return this.getMasonry();
            }
          }}
        </MediaQuery>
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
      return (
        <div className="top-stories-container">
          {this.state.showModal && (
            <ArticleModal setShow={this.setShow} story={this.state.selectedStory}/>
          )}
          <Masonry
                 // default ''
                elementType={'div'} // default 'div'
                options={masonryOptions} // default {}
                disableImagesLoaded={false} // default false
                updateOnEachImageLoad={false} // default false and works only if disableImagesLoaded is false
                // imagesLoadedOptions={imagesLoadedOptions} // default {}
            >
                {storyCards}
          </Masonry>
        </div>
        
      )
  }

  getMobileView() {
      return (
        this.state.storyList.map(story => {
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
      )
  }

}

export default TopStories