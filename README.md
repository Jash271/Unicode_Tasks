# Unicode_Tasks
## Following are the folders  this Repository contains:
  - Task 1
  - Task 2
  - Task 3
  - Task 4

# Task 1
##### The following has a python file that contains the code to check for the inputted binary numbers(input given by the user)if they are divisible by 5 or not and the following binary numbers satisfying this criterion are displayed  on the terminal
### Output:
![Screenshot (301) jpg](https://user-images.githubusercontent.com/51506649/63266556-cd3d7b00-c2ad-11e9-9cc4-ba7b815b563b.png)
##### As evident from the image ,the input binary numbers(1101,101)
 - 1101 (decimal equivalent -13)
 - 101 (decimal equivalent - 5)
 
##### Hence only 101 satisfies the criteria(Divisiblity with 5) and is subsequetly displayed on the terminal
#### [Link for calling the API](https://docs.spacexdata.com/?version=latest) 
# Task 2
##### For this task the web application so created communicates with SPACEX's API to extract data with regards to their launches (upcoming as well as those of the past)and is displayed on the front end.
##### with regards to the json date string obtained ,the date is sliced in two parts,converted into date time format and then parsed as string to display on the fornt end 
### Output:
![Screenshot (321)](https://user-images.githubusercontent.com/51506649/63270497-e9451a80-c2b5-11e9-944d-77f0ee4bb36a.png)
# Task 3
##### Continuing task 2 further the information obtained has been displayed on the frontend with the help of template
### Output :
![Screenshot (308)](https://user-images.githubusercontent.com/51506649/63266512-b008ac80-c2ad-11e9-98b8-0d2a8c89ce70.png)

# Task 4
#### Adding onto Task3 ,The response is stored into a database model .
![Screenshot (318)](https://user-images.githubusercontent.com/51506649/63266994-c4997480-c2ae-11e9-8971-2fa3407307ba.png)
#### The response is then fetched from the database and rendered using a template.
#### Additional Modifications:
 - Keeping a track whether the response is stored in the database
   - If so then there is no need to contact SPACEX API ,and display a message on the page stating that the details have been already downloaded ,you can directly view them .This prevents contacting the API on repeated basis and hence saves considerable loading time.
   if not ,then it loads the response into the so created database model
   
#### Illustration of the above point 
![Screenshot (311)](https://user-images.githubusercontent.com/51506649/63266601-e7775900-c2ad-11e9-825a-618635f8f4bd.png)

 - Loading all the attributes realted to a paticular launch takes up a lot of time ,hence to tackel this issue ,List Views have been implemented ,that shows partial information of a paticular launch and a link to view all it's related details ,by making use of Detail Views 
#### Illustration of the above point :

![Screenshot (314)](https://user-images.githubusercontent.com/51506649/63267087-f3afe600-c2ae-11e9-9b2b-954acf5437b6.png)

#### Clicking on more info gives all  related deatils of that paticular launch
![Screenshot (316)](https://user-images.githubusercontent.com/51506649/63267140-04f8f280-c2af-11e9-9608-5fd28547dc99.png)


     
