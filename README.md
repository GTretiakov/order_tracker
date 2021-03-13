# Order Tracker
This project is an application designed for internal use by a [distribution company](https://kolonakigroup.com/). The purpose of this application is to provide better coordination between differrent departments inside the company. The application helps to organize big amount of orders that come to the company daily in such a way that all orders can be grouped in different categories ('stores') and every order clearly represents its current status and can be updated by a respective department accordingly.

## UX
An inspiration for this project comes from [monday.com](https://monday.com/), an environment that helps companies to organize and manage their work process, and which is now used by my client. The company sells different categories of products (mostly wines and foods) via different platforms (such as Amazon and Shopify) as well as direct purchases from a warehouse. So it is very important to stay organized in this flow of data from multiple sources.
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
* A user can gerister personal account with a password secured by a password hashing.
* Create new stores and delete those you don't need.
* Create a new order inside a respective store.
* All users can create and update stores in any time.
* 'Last Edited By' column helps to determine the last user to edit an order.
* Future and today's delivery date have different colors, which makes it easier to determine which orders are urgent.
* Different status and progress colors make it easier to determine the current state of an order.
* An admin has an exclusive right to mark order as completed and delete it if necessary.
* Safely delete a store. All orders will stay in a database and you can easily recover them by creating a store with the appropriate name.

## Features left to Implement
* Make the aplication more secure, so registration is not available to everyone.
* Make The aplication mobile friendly, as now it is more suteble for a desktop computer.
* Ability to create new and manege existing order's statuses and progresses.

## Technologies Used
-	HTML
-	CSS
-	JavaScript
- Jquery
-	GitHub
-	GitPod
-	Google Fonts
-	Draw.io
-	Python
-	Flask
-	Materialize
-	Heroku
-	MongoDB
-	Font Awesome

## Testing
