import React, { Component } from 'react';
import './CategoryFilter.css';
import {CaretNext, CaretPrevious} from 'grommet-icons';
import ComponentSlider from "@kapost/react-component-slider";
import FilterOption from './FilterOption';

const renderLeftArrow = () => <CaretPrevious />;
const renderRightArrow = () => <CaretNext />;

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
        this.state = {
            selected: [],
          }
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
    return (
        <div className="menu-bar">
        <ComponentSlider
            renderLeftArrow={renderLeftArrow}
            renderRightArrow={renderRightArrow}
        >
            {Object.keys(categories).map((key, index) => {
                let selectedCategories = this.state.selected;
                let className = `
                ${selectedCategories.length == 0 ? 'default-selected' : selectedCategories.includes(key) ? '' : 'deselected'} ${categories[key]} menu-item
                `
                return (<FilterOption key={key} category={key} className={className} clickHandler={this.clickHandler}/>)
            })}
        </ComponentSlider>
        </div>
    );
  }
}

export default CategoryFilter