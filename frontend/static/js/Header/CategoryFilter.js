import React, { Component } from 'react';
import './CategoryFilter.css';
import {CaretNext, CaretPrevious} from 'grommet-icons';
import ComponentSlider from "@kapost/react-component-slider";
import FilterOption from './FilterOption';
import MediaQuery from "react-responsive";
import DragScroll from 'react-dragscroll';

const renderLeftArrow = () => <CaretPrevious color="#daa530"/>;
const renderRightArrow = () => <CaretNext color="#daa530"/>;

const categories = {
    'Sports': 'sports',
    'Business and Finance': 'business-and-finance',
    'Ireland': 'ireland',
    'Entertainment': 'entertainment',
    'Health': 'health',
    'Education': 'education',
    'World': 'world'
}

class CategoryFilter extends Component {

    constructor(props) {
        super(props)
          this.clickHandler = this.clickHandler.bind(this)
      }

    clickHandler(key) {
        let selectedArray = this.state.selected
        if (selectedArray.includes(key)) {
            let filteredArray = selectedArray.filter( el => el != key)
            return this.setState({selected: filteredArray})
        } else {
            selectedArray.push(key)
            return this.setState({selected: selectedArray})
        }
    }

  
  render() {

    return(
        <MediaQuery query="(hover: none) and (pointer: coarse)">
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

    getDesktopView() {
        return (
            <ComponentSlider
                renderLeftArrow={renderLeftArrow}
                renderRightArrow={renderRightArrow}
            >
                {Object.keys(categories).map((key, index) => {
                    let selectedCategories = this.props.filters;
                    let className = `
                    ${selectedCategories.length == 0 ? 'default-selected' : selectedCategories.includes(key) ? '' : 'deselected'} ${categories[key]} menu-item
                    `
                    return (<FilterOption key={key} category={key} className={className} clickHandler={this.props.updateFilters}/>)
                })}
            </ComponentSlider>
        )
    }

    getMobileView() {
        return (
            <DragScroll
                className="drag-scroll"
            >
                {Object.keys(categories).map((key, index) => {
                    let selectedCategories = this.props.filters;
                    let className = `
                    ${selectedCategories.length == 0 ? 'default-selected' : selectedCategories.includes(key) ? '' : 'deselected'} ${categories[key]} menu-item
                    `
                    return (<FilterOption key={key} category={key} className={className} clickHandler={this.props.updateFilters}/>)
                })}
            </DragScroll>
        )
    }

}

export default CategoryFilter