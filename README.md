# Friztalk-DjangoSocialNetwork
 
 An implementation of a social network web application in Django, Friztalk, offering functionalities such as:  
• Users can create new account  
• Users can log in and log out  
• Users can add other users as friends  
• Users can search for other users  
• Users can add media (such as images to their account and these are accessible via their home page)  
• Users can add status updates to their home page  

The complete process of how I created my social networking app, Friztalk, is discussed here [FriztalkSocialNetwork_Report.pdf](https://github.com/rizfebriansyah/Friztalk-DjangoSocialNetwork/files/9805614/FriztalkSocialNetwork_Report.pdf)

For the authentication and registration, I will be using Django allauth. I have followed the installation step by step from this document itself:
https://django-allauth.readthedocs.io/en/latest/installation.html

### Create new account
Users are able to create a new account. They need to provide an e-mail address, username, password to sign up.  
<img width="280" alt="friztalksignup" src="https://user-images.githubusercontent.com/88428142/196314208-d02c40fd-ee1b-4867-b5be-553651ae9643.png">

### Login/Logout
Once a user has created their account, they are able to login via their e-mail and password. Once logged in, they have the option to log out.  
<img width="523" alt="friztalklogin" src="https://user-images.githubusercontent.com/88428142/196314364-35e1a561-e91a-4632-b71a-e5bf6aa20530.png">

### Search for Users
Once logged in, user can go to the search bar, type a name, and a list of other users will be displayed. 
<img width="473" alt="friztalksearch" src="https://user-images.githubusercontent.com/88428142/196316905-39b5cea2-c60c-4231-8c34-1c5804b0cf9f.png">

### Add Users
User are able to add others as friends, or even remove them from your friend list.
<img width="430" alt="friztalkadd" src="https://user-images.githubusercontent.com/88428142/196317250-543274bc-903c-4d77-b3fb-57e5322510ca.png">

### Add Status
Users have the freedom to update their status. They are able to do so in the homepage.  
<img width="283" alt="friztalkstatus" src="https://user-images.githubusercontent.com/88428142/196317360-236379ea-8fee-44d6-9555-a0c6e982262f.png">

### Add Media
Users can upload images to their hearts’ content.  
<img width="368" alt="friztalkmedia" src="https://user-images.githubusercontent.com/88428142/196317389-44028886-f1c1-40b6-8ca3-0d66e2be822f.png">

### Update Post
The original user who posts a status also have the choice to update. 
<img width="525" alt="friztalkupdate" src="https://user-images.githubusercontent.com/88428142/196317679-983ab421-cefc-49f2-9841-4dda24d175cd.png">

### View Profile
Users are also able to view their own profile information by clicking on their profile picture on the navigation bar, just beside the search bar.
<img width="519" alt="friztalkprofile" src="https://user-images.githubusercontent.com/88428142/196317877-4b913a5b-0802-4520-9a7f-b542114e9a4f.png">

