<h3 align="center">Web Scraping script v0.2</h3>

  <p align="center">
    Scrape any website. (powered by Scrapy)
    <br />
    <a href="https://github.com/SwinSwinning/ScrapeScript"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SwinSwinning/ScrapeScript">View Demo</a>
    ·
    <a href="https://github.com/SwinSwinning/ScrapeScript/issues">Report Bug</a>
    ·
    <a href="https://github.com/SwinSwinning/ScrapeScript/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Simply download the "input.xlsx" and "scrapescript.exe" files from the Releases. 

In case you want to build the repo yourself check below.

### Prerequisites

Python 3 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SwinSwinning/ScrapeScript.git
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt 
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This early build of the script can help simplify scraping websites and saving the output to a json file. 

1. Open the input.xlsx file
2. fill out the values:
  A. start_url
    The complete URL of the website you would like to scrape 
    
  B. item_links
    Boolean Value to indicate if the scraper needs to access nested URL's to retrieve information from the items to scrape.
 
  C. item_css
    CSS or XPATH selector pointing to all the items in the page that need to be scraped. 
    
  D. next_page_url
    CSS or XPATH selector pointing to the link or button that leads to the next page. 
    
  E. next_page_url_add
    text addition to above mentioned selector indicating the element type that contains the actual URL to the next page.
    Is "href" in most cases.
    
  F. attributes_dict
    A string that contains names and associated selector's of the item values/information that need to be scraped. 
    Format is : "name1:selector1,name2:selector2,name3:selector3". 


<!-- ROADMAP -->
## Roadmap

- [ ] Support for Selection of User agent
- [ ] Support scraping of websites that require all scripts to finish running.
- [ ] Create web UI
    - [ ] Nested Feature

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Aswin -  Swin@thefocusforward.com

Project Link: [https://github.com/SwinSwinning/ScrapeScript](https://github.com/SwinSwinning/ScrapeScript)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



