# Web Scraper [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTheAlphamerc%2Fweb-scrapper&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
Web Scraper is a simple Flask-based API that allows users to retrieve meta data from any website by passing its URL as a request parameter.

## How to Use the API
To use the API, simply make a GET request to the following endpoint:

https://web-scrapper-coral.vercel.app/api/read_url_meta?url={website_url}

Here, {website_url} refers to the URL of the website whose metadata you want to retrieve. The API returns a JSON object containing the website's title, description, and image etc.

For example, to retrieve the metadata for https://www.theverge.com, you would make the following request:

https://web-scrapper-coral.vercel.app/api/read_url_meta?url=https://www.theverge.com

Project Setup
To set up the project, follow these steps:

- Clone the repository to your local machine.
```bash
git clone https://github.com/TheAlphamerc/web-scrapper
```

- Change into the project directory.
``` bash
 cd web-scrapper 
```

- Create a virtual environment and activate it.
``` bash
python3 -m venv venv
```

`source venv/bin/activate

- Install the project dependencies.
``` bash
pip install -r requirements.txt
```

- Setup the development environment by running these commands in your terminal.
 ``` bash
export FLASK_APP=index.py
export FLASK_ENV=development
```

- Run the Flask development server.
``` bash
python app.py
```

The API will be accessible at http://127.0.0.1:5000/api/read_url_meta?url={website_url}.

Contributing
Contributions to the project are welcome. If you'd like to contribute, please create a pull request with your changes.

## Created & Maintained By

[Sonu Sharma](https://github.com/TheAlphamerc) ([Twitter](https://www.twitter.com/TheAlphamerc)) ([Youtube](https://www.youtube.com/user/sonusharma045sonu/)) ([Insta](https://www.instagram.com/_sonu_sharma__)) ([Dev.to](https://dev.to/thealphamerc))
  ![Twitter Follow](https://img.shields.io/twitter/follow/thealphamerc?style=social) 


> If you found this project helpful or you learned something from the source code and want to thank me, consider buying me a cup of :coffee:
>
> * [PayPal](https://www.paypal.me/TheAlphamerc/)

> You can also nominate me for Github Star developer program
> https://stars.github.com/nominate



## Visitors Count

<img align="left" src = "https://profile-counter.glitch.me/TheAlphamerc-web-scrapper/count.svg" alt ="Loading">

