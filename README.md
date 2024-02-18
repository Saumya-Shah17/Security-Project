For using this project do some simple steps in your PC:
- Install and setup mysql in your PC.
- Then in app.py file line no. 4 change password to your root user's password in "".
- Then create database and table in your SQL using following queries:
  create database apps;
  use apps;
  create table data(Username varchar(30),Password varchar(30),Black int(1));
Then just run the app.py file and go to the host link in any browser and you are good to go👍.

Project Description:

This project contains login and register page where user can first register and then login. While registering there is a email validation and also the password should be of minimum 8 characters while registering.
Then on there is an admin account whose credentials are as follows:
Username - admin@host.com
Password - 12345678
On admin page you can see list of all users and also blacklist the desired user.
You can change the credentials of the admin in app.py file in line no. 21 in u and p respectively.
