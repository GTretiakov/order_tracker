# Order Tracker
This project is an application designed for internal use by a [distribution company](https://kolonakigroup.com/). The purpose of this application is to provide better coordination between different departments inside the company. The application helps to organize big number of orders that come to the company daily in such a way that all orders can be grouped in different categories ('stores') and every order clearly represents its current status and can be updated by a respective department accordingly.

## UX
An inspiration for this project comes from [monday.com](https://monday.com/), an environment that helps companies to organize and manage their work process, and which is now used by my client. The company sells different categories of products (mostly wines and foods) via different platforms (such as Amazon and Shopify) as well as direct purchases from a warehouse. It is very important to stay organized in this flow of data from multiple sources.
![monday](/images/monday.jpg)
 
### User Stories
* As a user, I want to create different stores, so I can see orders that are assigned to a particular store.
* As a user, I want recent and completed orders to appear separately.
* As a user, I want to create new orders and update recent orders.
* As a user, I want order's current status and progress to appear in different colors.
* As an admin, I want to have an exclusive right to delete orders and mark them as completed.
![wireframe](/images/wireframe.jpg)
![wireframe](/images/wireframe2.jpg)

## Features
* A user can register personal account with a password secured by a password hashing.
* Create new stores and delete those you don't need.
* Create a new order inside a respective store.
* All users can create and update stores in any time.
* 'Last Edited By' column helps to determine the last user to edit an order.
* Future and today's delivery date have different colors, which makes it easier to determine which orders are urgent.
* Different status and progress colors make it easier to determine the current state of an order.
* An admin has an exclusive right to mark order as completed and delete it if necessary.
* Safely delete a store. All orders will stay in a database and you can easily recover them by creating a store with the appropriate name.

## Features left to Implement
* Make the application more secure, so registration is not available to everyone.
* Make the application mobile friendly, as now it is more suitable for a desktop computer.
* Ability to create new and manage existing order's statuses and progresses.

## Technologies Used
-	HTML
-	CSS
-	JavaScript
- Jquery
-	Python
-	Flask
-	Materialize
-	Heroku
-	MongoDB
-	GitHub
-	GitPod
-	Font Awesome
-	Google Fonts
-	Draw.io

## Testing
Most of the testing was done manually during development process.
As a sample I've used a mini-project ('Task Manager') provided by Code Institute as a part of Data Centric Development course.
I wanted to not just repeat the mini-project, but bring it to a new level, making it more dynamic. And this is where I faced one of the biggest problems.
I had to make Flask routes with multiple parameters ('store_id', 'order_id') as I wanted a user to select store first and then manipulate orders assigned to this particular store. The Code Institute course provided us with examples of functions where only one parameter is passed, so I was confused and didn't know how to achieve my goal. I'm very lucky that we have a teacher, Usmaan Mujtaba, who was assisting us with our projects. He explained me how to implement Flask functions with multiple arguments, and now I have much deeper understanding of how Flask routing works.<br>
Another big issue I had was Materialize Select element. It couldn't pass a selected value to my database when I tried to edit an order. Even though it worked perfectly fine when I added new order. I was really confused, as in both scenarios I'm using a select element inside a form, with a submit button and a 'post' method. I've even tried creating a new collection in my database so I can pull values from there, but it still didn't work. I know that Materialize transforms select element into unordered list that has list items as options and passing the appropriate value to an input adding 'selected' class to appropriate list item. But I still don't know why it behaves differently in scenarios mentioned above. After doing some research online I've found a solution on [Stack Overflow](https://stackoverflow.com/questions/43403306/materialize-select-dropdown-not-passing-value-to-controller-in-ruby/43404104). I had to create a hidden input and use JavaScript to pass selected value from a select element to my hidden input. I had to place this JS code inside Jinja for loop, as every order has a unique ID.

## Deployment

The application was deployed on Heroku and can be found via following link: http://kolonaki-order-tracker.herokuapp.com/
