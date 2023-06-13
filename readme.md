## Muay Thai Backend API

- **App Title**: Muay Thai Techniques.
- **App Description**: The Muay Thai Backend API is a comprehensive application that provides a wealth of information about various Muay Thai techniques. Whether you're an enthusiast, practitioner, or simply curious about the martial art, this API serves as a valuable resource.
- **API**: The data used for this API is sourced from a JSON file I created on my own from techniques.json in my project. I give a name, description and image for each technique.
- **API Snippet**:

```
{
    "name": "Kradot Te",
    "description": "Jump Kick",
    "img": "https://dojomart.com/wp-content/uploads/2022/01/Jump-Kick-1.gif"
}
```

- **CRUD**: 

| Route  |  HTTP Method | DB Action  | Description  |
|---|---|---|---|
| /categories | GET  | INDEX  | Indexes all the demons |
| /techniques  | POST | CREATE  | Create a list of demons |
| /categories/:name  | GET  | SHOW  | Show a single demon |
| /categories/:name | PUT  | UPDATE  | Update a demon from your list  |
| /categories/:name  | DELETE  | DELETE  | Delete a demon off your list |


- **MVP**: Just implement the CRUD onto my Muay Thai Backend API. I want to make sure it's being deployed correctly, and all the data sets appear on Vercel as well as have my database appear on PostgreSQL.
- **Post-MVP**: I would like to add more information to each technique and add more features to this backend API such as creating training programs, grouping techniques, and tracking progress and performance.
- **Goals**: Implement all the necessary models, serializerz, views as well as the urls.py file an setting file.
- **Major Hurdles**: My biggest hurdle was figuring out how to add a new technique into the json physically. It took me a while to figure that out. I had trouble deploying this backend API onto Railways.
<!-- - **Data Model**: e.g. Get this from Excalidraw

![model](https://user-images.githubusercontent.com/54910341/221757530-e9152ee4-74f4-4fca-9b06-331bf1f64825.png) -->

- **Screenshot**: Here is a screenshot of the API database that is shown on Railways.
