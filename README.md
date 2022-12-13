# OSW_OpenCV
### Play a game touch by hand to image file, with planet image.

We are using OpenCV and python program.

## **How to play it**
1. Play steps
    1. Progress the python program file name "Game.py"
    2. Start with 30 seconds when we enter the game
    3. Touch the planet image and you get the score!
    4. And planet image move randomly to other location.
    5. When you hit the planet image, you get the total score, and it appears when the time end.

2. Assumptions:
    1. There is a reference object in the image which is easy to find and it's width/height is know to us.
3. Uses "Pixel Per Metric" ratio to calculate the size based on the given reference object.
4. Reference object properties:
    1. We should know the dimensions of this object (in terms of width or height).
    2. We should be able to easily find this reference object in the image, either based on the placement of the object (like being placed in top-left corner, etc.) or via appearances (like distinctive color and/or shape).
5. Used the United States quarter as the reference object.
6. Used the OpenCV's find contours method to find the objects in the image and calculated their dimensions.

## **Requirements what you have to install package file**
 1. python
 2. opencv
 3. numpy
 4. cvzone
 5. math

## **Commands to run the file**
```
python Game.py
```

## **Results:**
You can play the game with shor time, 30 seconds. And you can play 3D method because you need to use your hand. And also, you need to control distance between camera and your hand.


![Gif 1 of object dimensions](example1.gif)


## **Limitations and improvements**
1. You can only use one hand, not two hand. We can improve this program using two hands, and increase the difficulty of the game.
2. Photos are only use 3 images, with planet image. We can add more image and people can get more interest.

## **References:**

All thanks to Murtaza's Workshop (from [Youtube1](https://www.youtube.com/watch?v=6DxN8G9vB50&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q&index=2), from [Youtube2](https://www.youtube.com/watch?v=3xfOa4yeOb0&t=1135s), from [Youtube3](https://www.youtube.com/watch?v=NGQgRH2_kq8&t=2513s) for making game projects. 

We are also check some of function to Blog: 
[Opencv control image](https://youbidan.tistory.com/19). 
[Opencv take image](https://ansan-survivor.tistory.com/953). 
