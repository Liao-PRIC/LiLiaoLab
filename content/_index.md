---
# Leave the homepage title empty to use the site title
title:
date: 2025-04-01
type: landing

sections:
  - block: hero
    content:
      title: |
        Li Liao
        Research Group
      image:
        filename: 
      text: |
        <br>
        
        The **LiLiao Lab** is interested in various aspects of microorganisms living in Antarctic and the Arctic regions: including **bacterial sRNAs** and their regulation, **microbial diversity** and survival in extreme environments (e.g., in subglacial lakes, sea ice, sea water), as well as innovation of microbial cultivation and microbial resource exploration.
  
  - block: slider
    content:
      slides:
      - title: 👋 Welcome to the lab!
        content: Take a look at what we're working on...
        align: center
        background:
          image:
            filename: welcome_to_the_group.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Our researches ☕️
        content: 'We care about life in the extreme conditions!'
        align: left
        background:
          image:
            filename: our_research.png
            filters:
              brightness: 0.7
          position: center
          color: '#555'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Our Projects
          url: ../research/
      - title: We are looking for kindred spirits!
        content: 'Welcome to join us!'
        align: right
        background:
          image:
            filename: welcome_to_join_us.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Contact Us
          url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000

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

  - block: collection
    content:
      title: Latest Pubilications
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
---
