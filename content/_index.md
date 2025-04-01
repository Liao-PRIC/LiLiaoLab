---
# Leave the homepage title empty to use the site title
title:
date: 2020-12-01
type: landing

sections:
  - block: hero
    content:
      title: |
        Li Liao
        Research Group
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        The **LiLiao Lab** is interested in various aspects of microorganisms living in Antarctic and the Arctic regions: including bacterial sRNAs and their regulation, microbial diversity and survival in extreme environments (e.g., in subglacial lakes, sea ice, sea water), as well as innovation of microbial cultivation and microbial resource exploration.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
