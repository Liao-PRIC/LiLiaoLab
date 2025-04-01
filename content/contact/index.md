---
title: Contact
date: 2025-04-01

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
        We sincerely welcome researchers who have passion for polar science, microbiology, bioinformatcis, biogeochemistry...Now Join Us!
      email: liaoli@pric.org.cn
#      phone: 888 888 88 88
      address:
        street: 451 Jinqiao Road
        city: Pudong New Area
        region: Shanghai
        postcode: '200136'
        country: China
        country_code: CN
#      coordinates:
#        latitude: '37.4275'
#        longitude: '-122.1697'
      directions: Floor 5
      office_hours:
        - 'Monday-Friday 10:00 to 17:00'
      appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
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
          filename: contact.jpg
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
