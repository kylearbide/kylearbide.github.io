// gitprofile.config.ts

const CONFIG = {
  github: {
    username: 'kylearbide', // Your GitHub org/user name. (This is the only required config)
  },
  /**
   * If you are deploying to https://<USERNAME>.github.io/, for example your repository is at https://github.com/arifszn/arifszn.github.io, set base to '/'.
   * If you are deploying to https://<USERNAME>.github.io/<REPO_NAME>/,
   * for example your repository is at https://github.com/arifszn/portfolio, then set base to '/portfolio/'.
   */
  base: '/',
  projects: {
    github: {
      display: true, // Display GitHub projects?
      header: 'Github Projects',
      mode: 'manual', // Mode can be: 'automatic' or 'manual'
      automatic: {
        sortBy: 'stars', // Sort projects by 'stars' or 'updated'
        limit: 8, // How many projects to display.
        exclude: {
          forks: false, // Forked projects will not be displayed if set to true.
          projects: [], // These projects will not be displayed. example: ['arifszn/my-project1', 'arifszn/my-project2']
        },
      },
      manual: {
        // Properties for manually specifying projects
        projects: [
          'kylearbide/npcgpt', 
          'Mykalgitswaves/HTML-Interactive-templates',
          'kylearbide/PGA_Tour_Analysis',
          'kylearbide/DC-Metro-Ridership-Covid',
          'kylearbide/midterm_election_semantics_2022',
          'kylearbide/reddit_graph_db'
        ], // List of repository names to display. example: ['arifszn/my-project1', 'arifszn/my-project2']
      },
    },
    external: {
      header: 'My Projects',
      // To hide the `External Projects` section, keep it empty.
      projects: [
        // {
        //   title: 'Project Name',
        //   description:
        //     'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc ut.',
        //   imageUrl:
        //     'https://img.freepik.com/free-vector/illustration-gallery-icon_53876-27002.jpg',
        //   link: 'https://example.com',
        // },
        // {
        //   title: 'Project Name',
        //   description:
        //     'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc ut.',
        //   imageUrl:
        //     'https://img.freepik.com/free-vector/illustration-gallery-icon_53876-27002.jpg',
        //   link: 'https://example.com',
        // },
      ],
    },
  },
  seo: {
    title: 'Portfolio of Kyle Arbide',
    description: '',
    imageURL: '',
  },
  social: {
    linkedin: 'kyle-arbide',
    twitter: '',
    mastodon: '',
    researchGate: '',
    facebook: '',
    instagram: '',
    reddit: '',
    threads: '',
    youtube: '', // example: 'pewdiepie'
    udemy: '',
    dribbble: '',
    behance: '',
    medium: 'kyle.arbide',
    dev: '',
    stackoverflow: '', // example: '1/jeff-atwood'
    skype: '',
    telegram: '',
    website: '',
    phone: '',
    email: 'kyle.arbide@gmail.com',
  },
  resume: {
    fileUrl:
      'https://kylearbide.github.io/gitprofile/RESUME_Arbide_Kyle_May_2024.pdf', // Empty fileUrl will hide the `Download Resume` button.
  },
  skills: [
    'Python',
    'NLP',
    'R',
    'PostgreSQL',
    'MySQL',
    'SQLite',
    'Neo4j',
    'AllegroGraph',
    'MongoDB',
    'AWS',
    'Terraform',
    'Git',
    'Docker',
    "HuggingFace"
  ],
  experiences: [
    {
      company: 'Noblis',
      position: 'Data Scientist',
      from: 'June 2022',
      to: 'Present',
      companyLink: 'https://noblis.org/',
    },
    {
      company: 'Base Operations',
      position: 'Statistics Intern',
      from: 'August 2021',
      to: 'May 2022',
      companyLink: 'https://www.baseoperations.com/',
    },
  ],
  certifications: [
    {
      name: 'AWS Certified Cloud Practitioner',
      body: 'The AWS Certified Cloud Practitioner validates foundational, high-level understanding of AWS Cloud, services, and terminology.',
      year: 'May 2024',
      link: 'https://www.credly.com/badges/13ba3cb6-6f12-423c-bf1e-065c77f5bc52/public_url',
    },
  ],
  educations: [
    {
      institution: 'George Washington University',
      degree: 'MS Data Analytics',
      from: '2021',
      to: '2023',
    },
    {
      institution: 'University of Miami',
      degree: 'Bachlor\'s degree, Industrial Engineering',
      from: '2017',
      to: '2021',
    },
  ],
  publications: [
    // {
    //   title: 'HTML Interactive',
    //   conferenceName: '',
    //   journalName: 'Medium',
    //   authors: 'Kyle Arbide, Michael Goldstein',
    //   link: 'https://medium.com/gopenai/html-interactive-a-custom-gpt-for-building-interactive-web-pages-2f66cac16ced',
    //   description:
    //     'A Custom GPT for building interactive web pages',
    // }
  ],
  // Display articles from your medium or dev account. (Optional)
  blog: {
    source: 'medium', // medium | dev
    username: 'kyle.arbide', // to hide blog section, keep it empty
    limit: 2, // How many articles to display. Max is 10.
  },
  googleAnalytics: {
    id: '', // GA3 tracking id/GA4 tag id UA-XXXXXXXXX-X | G-XXXXXXXXXX
  },
  // Track visitor interaction and behavior. https://www.hotjar.com
  hotjar: {
    id: '',
    snippetVersion: 6,
  },
  themeConfig: {
    defaultTheme: 'light',

    // Hides the switch in the navbar
    // Useful if you want to support a single color mode
    disableSwitch: false,

    // Should use the prefers-color-scheme media-query,
    // using user system preferences, instead of the hardcoded defaultTheme
    respectPrefersColorScheme: false,

    // Display the ring in Profile picture
    displayAvatarRing: true,

    // Available themes. To remove any theme, exclude from here.
    themes: [
      'light',
      'dark',
      'cupcake',
      'bumblebee',
      'emerald',
      'corporate',
      'synthwave',
      'retro',
      'cyberpunk',
      'valentine',
      'halloween',
      'garden',
      'forest',
      'aqua',
      'lofi',
      'pastel',
      'fantasy',
      'wireframe',
      'black',
      'luxury',
      'dracula',
      'cmyk',
      'autumn',
      'business',
      'acid',
      'lemonade',
      'night',
      'coffee',
      'winter',
      'dim',
      'nord',
      'sunset',
      'procyon',
    ],

    // Custom theme, applied to `procyon` theme
    customTheme: {
      primary: '#fc055b',
      secondary: '#219aaf',
      accent: '#e8d03a',
      neutral: '#2A2730',
      'base-100': '#E3E3ED',
      '--rounded-box': '3rem',
      '--rounded-btn': '3rem',
    },
  },

  // Optional Footer. Supports plain text or HTML.
  footer: `Made with <a 
      class="text-primary" href="https://github.com/arifszn/gitprofile"
      target="_blank"
      rel="noreferrer"
    >GitProfile</a> and ❤️`,

  enablePWA: true,
};

export default CONFIG;
