[Am I in Sheffield?](http://amiinsheffield.biz)<br>
[Github for source code](https://github.com/OGD311/Triangulator)

## Inspiration
Number 1 MiroFan and CompSoc President Erik Lippert and his amazingly 'simple' Datetime website.

## What we learned
Fine tuning ML models is HARD<br>
Maths can be 'fun'<br>
You can never drink too much Monster Energy™<br>

## How we Built
Using the power of Monster Energy™ and by exceeding our daily doses of Taurine, Vitamin B, and Caffeine, we managed to write a basic program to aggressively ping hundreds of datacenters across the United Kingdom and Republic of Ireland, before condendsing our data using DataScience™ skills (an if statement) to then extract the best performing data centers.<br>

Next we used the Haversine equation, recommended to us by our dear friend ChatGPT. This equation allows us to calculate the approximate distance between coordinates, allowing us to calculate the distance from our location of 38 Mappin Street to these datacenter.<br>


Then we used Machine Learning and Polynomial Regression to calculate the gradient between response time and distance, giving us a model that could predict distance based off a response time.<br>

Next we use this model, along with new pings to three datacenters (Wales, London, Newcastle (Home of Greggs) ). The response times for these pings are then fed into our advanced AI model, responding with the estimated distance from these datacenters.<br>

Finally we use more Advanced Math™ to calculate where these circles overlap (if at all), and the centre-point of this overlap. This result is then fed into an algorithm (see below) to determine if you are close enough to Sheffield, before returning the answer to the user.<br>

Are you in Sheffield Algorithm:
``` python
if distance < 20:
    print("You are in Sheffield")

elif distance < 50:
    print("Maybe in Sheffield")

else:
    print("Not in Sheffield")
```
## Possible Uses
- **CIA** -> The CIA always want to know where persons of interest are, but they are not always easy to find. Well with 'AmIInSheffield', the CIA can quickly find out if the POI is in the Sheffield Area.
- **Temu** -> We all love shopping, and no one loves shopping more than Temu, the large Chinese ECommerce Platform. Also, they run a side business of selling ALL your personal data when you use their site :) This app could be used by them to locate pesky customers who have their location services off! Keep up the good work!!
- **999** -> Have you ever been stuck in an emergency situation where you are lost and don't have GPS but do have the wonderful 5G™? Well, with AmIInSheffield, you can easily tell the emergency services if you are located within the Sheffield area, helping them to locate you!
- **Santa** -> Santa needs to know where all the good children are in the world, so that he can deliver presents to them. By using AmIInSheffield, Santa can easily see if he is in Sheffield, and then use this to avoid delivering any presents to children in the Sheffield area :)

## Future Plans
- **Expand Franchise** -> Expand the "Am I in?" franchise to include all the cities.<br>
- **Commercial Optimisation**-> Serve the user more ads, and implement a premium version.<br>
