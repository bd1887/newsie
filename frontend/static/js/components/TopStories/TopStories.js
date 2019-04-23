import React, { Component } from 'react';
import axios from 'axios';
import './TopStories.css'
import TopStoryCard from './TopStoryCard'
import ArticleModal from '../ArticleModal/ArticleModal';
import Masonry from 'react-masonry-component';
import { Link } from 'react-router-dom'

const masonryOptions = {
  transitionDuration: 0
};

// const imagesLoadedOptions = { background: 'url(https://via.placeholder.com/150)' }

class TopStories extends Component {
  constructor(props) {
    super(props)
    this.state = {
      storyList: [],
      loading: true,
      showModal: false,
      selectedStory: null
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
    axios.get('/api/top-stories/?date-range=this_month')
    .then(response => {
      console.log(response.data)
      this.setState({   
        storyList: response.data,
        loading: false
      })
    })
  }

  render() {
    if (this.state.loading) {
      return (<p>loading...</p>)
    } else {
      const storyCards = this.state.storyList.map(story => {
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
          />
      })
      return (
        <div>
          {this.state.showModal && (
            <ArticleModal setShow={this.setShow} story={this.state.selectedStory}/>
          )}
          <Masonry
                className={'masonry-container'} // default ''
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
  }
}

export default TopStories